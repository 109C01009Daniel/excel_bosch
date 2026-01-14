"""
Excel 搜索系統 - 數據庫模組
使用 SQLite FTS5 實現全文檢索
"""
import sqlite3
import os
import logging
from datetime import datetime
from typing import List, Dict, Any, Optional, Tuple
from contextlib import contextmanager

from config import DATABASE_PATH, DATABASE_CONFIG

logger = logging.getLogger(__name__)


class Database:
    """數據庫操作類"""

    def __init__(self, db_path: str = DATABASE_PATH):
        """
        初始化數據庫連接

        Args:
            db_path: 數據庫文件路徑
        """
        self.db_path = db_path
        self.conn = None
        self._initialize_connection()
        self.initialize_db()

    def _initialize_connection(self):
        """初始化數據庫連接並設置 PRAGMA 優化"""
        self.conn = sqlite3.connect(self.db_path, check_same_thread=False)
        self.conn.row_factory = sqlite3.Row  # 使結果可以用字段名訪問

        # 應用 PRAGMA 優化設置
        cursor = self.conn.cursor()
        pragma_settings = DATABASE_CONFIG.get('pragma_settings', {})

        for pragma, value in pragma_settings.items():
            try:
                cursor.execute(f"PRAGMA {pragma} = {value}")
                logger.debug(f"設置 PRAGMA {pragma} = {value}")
            except Exception as e:
                logger.warning(f"無法設置 PRAGMA {pragma}: {e}")

        self.conn.commit()

    def initialize_db(self):
        """初始化數據庫結構（創建表和索引）"""
        cursor = self.conn.cursor()

        # 1. 文件元數據表
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS files (
                file_id INTEGER PRIMARY KEY AUTOINCREMENT,
                file_path TEXT UNIQUE NOT NULL,
                file_name TEXT NOT NULL,
                last_modified TIMESTAMP NOT NULL,
                file_size INTEGER,
                cell_count INTEGER DEFAULT 0,
                indexed_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        ''')

        # 2. 單元格詳細信息表
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS cells (
                cell_id INTEGER PRIMARY KEY AUTOINCREMENT,
                file_id INTEGER NOT NULL,
                sheet_name TEXT NOT NULL,
                row_num INTEGER NOT NULL,
                col_num INTEGER NOT NULL,
                cell_location TEXT NOT NULL,
                value TEXT,
                value_lower TEXT,
                is_merged BOOLEAN DEFAULT FALSE,
                merged_range TEXT,
                FOREIGN KEY (file_id) REFERENCES files(file_id) ON DELETE CASCADE
            )
        ''')

        # 3. FTS5 全文搜索虛擬表
        try:
            cursor.execute('''
                CREATE VIRTUAL TABLE IF NOT EXISTS content_fts USING fts5(
                    file_id UNINDEXED,
                    sheet_name,
                    cell_location,
                    cell_value,
                    tokenize='porter unicode61'
                )
            ''')
            logger.info("FTS5 全文索引表創建成功")
        except Exception as e:
            logger.error(f"創建 FTS5 表失敗: {e}")
            raise

        # 4. 創建索引以加速查詢
        indexes = [
            "CREATE INDEX IF NOT EXISTS idx_cells_file_id ON cells(file_id)",
            "CREATE INDEX IF NOT EXISTS idx_cells_value_lower ON cells(value_lower)",
            "CREATE INDEX IF NOT EXISTS idx_cells_sheet ON cells(file_id, sheet_name)",
            "CREATE INDEX IF NOT EXISTS idx_cells_row ON cells(file_id, sheet_name, row_num)",
            "CREATE INDEX IF NOT EXISTS idx_merged ON cells(merged_range) WHERE is_merged = TRUE",
        ]

        for idx_sql in indexes:
            try:
                cursor.execute(idx_sql)
            except Exception as e:
                logger.warning(f"創建索引失敗: {e}")

        self.conn.commit()
        logger.info(f"數據庫初始化完成: {self.db_path}")

    @contextmanager
    def transaction(self):
        """事務上下文管理器"""
        try:
            yield self.conn
            self.conn.commit()
        except Exception as e:
            self.conn.rollback()
            logger.error(f"事務回滾: {e}")
            raise

    # ========================================================================
    # 文件操作
    # ========================================================================

    def add_file(self, file_path: str, file_name: str,
                 last_modified: datetime, file_size: int) -> int:
        """
        添加或更新文件記錄

        Args:
            file_path: 文件完整路徑
            file_name: 文件名
            last_modified: 最後修改時間
            file_size: 文件大小（字節）

        Returns:
            file_id: 文件 ID
        """
        cursor = self.conn.cursor()

        # 使用 INSERT OR REPLACE 來處理重複
        cursor.execute('''
            INSERT OR REPLACE INTO files
            (file_path, file_name, last_modified, file_size, indexed_at)
            VALUES (?, ?, ?, ?, ?)
        ''', (file_path, file_name, last_modified, file_size, datetime.now()))

        self.conn.commit()
        file_id = cursor.lastrowid

        # 如果是更新（lastrowid 為 0），則查詢 file_id
        if file_id == 0:
            cursor.execute('SELECT file_id FROM files WHERE file_path = ?', (file_path,))
            result = cursor.fetchone()
            file_id = result[0] if result else None

        logger.debug(f"添加/更新文件: {file_name} (ID: {file_id})")
        return file_id

    def get_file_id(self, file_path: str) -> Optional[int]:
        """
        獲取文件 ID

        Args:
            file_path: 文件路徑

        Returns:
            file_id 或 None
        """
        cursor = self.conn.cursor()
        cursor.execute('SELECT file_id FROM files WHERE file_path = ?', (file_path,))
        result = cursor.fetchone()
        return result[0] if result else None

    def file_needs_reindex(self, file_path: str, current_modified: datetime) -> bool:
        """
        檢查文件是否需要重新索引

        Args:
            file_path: 文件路徑
            current_modified: 當前文件修改時間

        Returns:
            True 需要重新索引，False 不需要
        """
        cursor = self.conn.cursor()
        cursor.execute('''
            SELECT last_modified FROM files WHERE file_path = ?
        ''', (file_path,))
        result = cursor.fetchone()

        if not result:
            return True  # 文件未索引，需要索引

        # 比較修改時間
        stored_modified = datetime.fromisoformat(result[0])
        needs_update = current_modified > stored_modified

        if needs_update:
            logger.debug(f"文件已修改，需要重新索引: {file_path}")

        return needs_update

    def get_all_files(self) -> List[Dict[str, Any]]:
        """
        獲取所有已索引的文件

        Returns:
            文件列表
        """
        cursor = self.conn.cursor()
        cursor.execute('''
            SELECT file_id, file_path, file_name, last_modified,
                   file_size, cell_count, indexed_at
            FROM files
            ORDER BY indexed_at DESC
        ''')

        return [dict(row) for row in cursor.fetchall()]

    def delete_file(self, file_id: int):
        """
        刪除文件及其所有相關數據

        Args:
            file_id: 文件 ID
        """
        cursor = self.conn.cursor()

        # 刪除單元格數據
        cursor.execute('DELETE FROM cells WHERE file_id = ?', (file_id,))
        # 刪除 FTS5 數據
        cursor.execute('DELETE FROM content_fts WHERE file_id = ?', (file_id,))
        # 刪除文件記錄
        cursor.execute('DELETE FROM files WHERE file_id = ?', (file_id,))

        self.conn.commit()
        logger.debug(f"刪除文件 ID: {file_id}")

    def delete_file_content(self, file_id: int):
        """
        刪除文件的所有內容（保留文件記錄，用於重新索引）

        Args:
            file_id: 文件 ID
        """
        cursor = self.conn.cursor()
        cursor.execute('DELETE FROM cells WHERE file_id = ?', (file_id,))
        cursor.execute('DELETE FROM content_fts WHERE file_id = ?', (file_id,))
        # 重置單元格計數
        cursor.execute('UPDATE files SET cell_count = 0 WHERE file_id = ?', (file_id,))
        self.conn.commit()
        logger.debug(f"刪除文件內容 ID: {file_id}")

    # ========================================================================
    # 單元格操作
    # ========================================================================

    def add_cells_batch(self, cells_data: List[Dict[str, Any]]):
        """
        批量添加單元格數據

        Args:
            cells_data: 單元格數據列表，每個元素包含：
                - file_id: 文件 ID
                - sheet_name: 工作表名
                - row: 行號
                - col: 列號
                - location: 單元格位置（如 "A5"）
                - value: 單元格值
                - is_merged: 是否為合併儲存格（可選）
                - merged_range: 合併範圍（可選）
        """
        if not cells_data:
            return

        cursor = self.conn.cursor()

        # 準備數據
        cells_rows = []
        fts_rows = []

        for cell in cells_data:
            value = str(cell['value']).strip() if cell.get('value') else ''
            if not value:
                continue

            # 準備 cells 表數據
            cells_rows.append((
                cell['file_id'],
                cell['sheet_name'],
                cell['row'],
                cell['col'],
                cell['location'],
                value,
                value.lower(),  # 小寫版本用於不區分大小寫搜索
                cell.get('is_merged', False),
                cell.get('merged_range', None)
            ))

            # 準備 FTS5 表數據
            fts_rows.append((
                cell['file_id'],
                cell['sheet_name'],
                cell['location'],
                value
            ))

        # 批量插入到 cells 表
        try:
            cursor.executemany('''
                INSERT INTO cells
                (file_id, sheet_name, row_num, col_num, cell_location,
                 value, value_lower, is_merged, merged_range)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
            ''', cells_rows)

            # 批量插入到 FTS5 表
            cursor.executemany('''
                INSERT INTO content_fts
                (file_id, sheet_name, cell_location, cell_value)
                VALUES (?, ?, ?, ?)
            ''', fts_rows)

            self.conn.commit()
            logger.debug(f"批量插入 {len(cells_data)} 個單元格")

        except Exception as e:
            self.conn.rollback()
            logger.error(f"批量插入失敗: {e}")
            raise

    def get_row_cells(self, file_id: int, sheet_name: str, row_num: int) -> List[Dict[str, Any]]:
        """
        獲取指定行的所有單元格

        Args:
            file_id: 文件 ID
            sheet_name: 工作表名
            row_num: 行號

        Returns:
            單元格列表，按列號排序
        """
        cursor = self.conn.cursor()
        cursor.execute('''
            SELECT cell_location, col_num, value
            FROM cells
            WHERE file_id = ? AND sheet_name = ? AND row_num = ?
            ORDER BY col_num
        ''', (file_id, sheet_name, row_num))

        return [dict(row) for row in cursor.fetchall()]

    def update_file_cell_count(self, file_id: int):
        """
        更新文件的單元格計數

        Args:
            file_id: 文件 ID
        """
        cursor = self.conn.cursor()
        cursor.execute('''
            UPDATE files
            SET cell_count = (SELECT COUNT(*) FROM cells WHERE file_id = ?)
            WHERE file_id = ?
        ''', (file_id, file_id))
        self.conn.commit()

    # ========================================================================
    # 統計信息
    # ========================================================================

    def get_stats(self) -> Dict[str, Any]:
        """
        獲取數據庫統計信息

        Returns:
            統計信息字典
        """
        cursor = self.conn.cursor()

        # 文件數
        cursor.execute('SELECT COUNT(*) FROM files')
        file_count = cursor.fetchone()[0]

        # 單元格數
        cursor.execute('SELECT COUNT(*) FROM cells')
        cell_count = cursor.fetchone()[0]

        # 文件總大小
        cursor.execute('SELECT SUM(file_size) FROM files')
        total_size = cursor.fetchone()[0] or 0

        # 數據庫文件大小
        db_size = os.path.getsize(self.db_path) if os.path.exists(self.db_path) else 0

        # 最後索引時間
        cursor.execute('SELECT MAX(indexed_at) FROM files')
        last_indexed = cursor.fetchone()[0]

        return {
            'file_count': file_count,
            'cell_count': cell_count,
            'total_file_size_mb': round(total_size / (1024 * 1024), 2),
            'db_size_mb': round(db_size / (1024 * 1024), 2),
            'last_indexed': last_indexed,
            'avg_cells_per_file': round(cell_count / file_count, 2) if file_count > 0 else 0,
        }

    def vacuum(self):
        """
        壓縮數據庫（回收空間）
        """
        logger.info("開始壓縮數據庫...")
        self.conn.execute('VACUUM')
        logger.info("數據庫壓縮完成")

    def analyze(self):
        """
        分析數據庫（更新統計信息以優化查詢）
        """
        logger.info("分析數據庫...")
        self.conn.execute('ANALYZE')
        logger.info("數據庫分析完成")

    # ========================================================================
    # 資源管理
    # ========================================================================

    def close(self):
        """關閉數據庫連接"""
        if self.conn:
            self.conn.close()
            logger.info("數據庫連接已關閉")

    def __enter__(self):
        """上下文管理器入口"""
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        """上下文管理器出口"""
        self.close()

    def __del__(self):
        """析構函數"""
        self.close()


# ============================================================================
# 輔助函數
# ============================================================================

def check_fts5_support() -> bool:
    """
    檢查 SQLite 是否支持 FTS5

    Returns:
        True 支持，False 不支持
    """
    try:
        conn = sqlite3.connect(':memory:')
        cursor = conn.cursor()
        cursor.execute('CREATE VIRTUAL TABLE test USING fts5(content)')
        conn.close()
        return True
    except Exception as e:
        logger.error(f"FTS5 不支持: {e}")
        return False


if __name__ == '__main__':
    # 測試數據庫模組
    import logging.config
    from config import LOGGING_CONFIG

    # 配置日志
    logging.config.dictConfig(LOGGING_CONFIG)

    # 檢查 FTS5 支持
    if not check_fts5_support():
        print("❌ SQLite 不支持 FTS5！請升級 SQLite 版本。")
        exit(1)

    print("✅ SQLite 支持 FTS5")

    # 測試數據庫操作
    print("\n測試數據庫操作...")

    with Database(':memory:') as db:  # 使用內存數據庫測試
        print("✅ 數據庫初始化成功")

        # 測試添加文件
        file_id = db.add_file(
            file_path='/test/sample.xlsx',
            file_name='sample.xlsx',
            last_modified=datetime.now(),
            file_size=1024
        )
        print(f"✅ 添加文件成功，ID: {file_id}")

        # 測試添加單元格
        cells = [
            {
                'file_id': file_id,
                'sheet_name': 'Sheet1',
                'row': 1,
                'col': 1,
                'location': 'A1',
                'value': 'Test Data',
            },
            {
                'file_id': file_id,
                'sheet_name': 'Sheet1',
                'row': 1,
                'col': 2,
                'location': 'B1',
                'value': 'PN3004',
            },
        ]
        db.add_cells_batch(cells)
        print(f"✅ 添加單元格成功，數量: {len(cells)}")

        # 更新統計
        db.update_file_cell_count(file_id)

        # 獲取統計信息
        stats = db.get_stats()
        print(f"✅ 統計信息: {stats}")

    print("\n✅ 所有測試通過！")
