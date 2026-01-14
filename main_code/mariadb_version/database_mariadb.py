#!/usr/bin/env python3
"""
MariaDB 資料庫操作模組
Excel 搜索系統 - MariaDB 版本
"""
import mysql.connector
from mysql.connector import Error
from config_mariadb import DB_CONFIG
from datetime import datetime


class DatabaseManager:
    """MariaDB 資料庫管理類"""

    def __init__(self):
        """初始化資料庫管理器"""
        self.connection = None
        self.cursor = None

    def connect(self):
        """連接到 MariaDB 資料庫"""
        try:
            self.connection = mysql.connector.connect(**DB_CONFIG)
            self.cursor = self.connection.cursor(dictionary=True)
            return True
        except Error as e:
            print(f"❌ 連接資料庫失敗: {e}")
            return False

    def close(self):
        """關閉資料庫連接"""
        if self.cursor:
            self.cursor.close()
        if self.connection and self.connection.is_connected():
            self.connection.close()

    def __enter__(self):
        """支援 with 語句"""
        self.connect()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        """支援 with 語句"""
        self.close()

    def create_tables(self):
        """建立資料表"""
        try:
            # 建立 files 表
            self.cursor.execute("""
                CREATE TABLE IF NOT EXISTS files (
                    file_id INT AUTO_INCREMENT PRIMARY KEY,
                    file_path VARCHAR(1000) NOT NULL UNIQUE,
                    file_name VARCHAR(500) NOT NULL,
                    last_modified DATETIME,
                    file_size BIGINT,
                    cell_count INT DEFAULT 0,
                    indexed_at DATETIME DEFAULT CURRENT_TIMESTAMP,
                    INDEX idx_file_name (file_name),
                    INDEX idx_indexed_at (indexed_at)
                ) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci
            """)

            # 建立 cells 表
            self.cursor.execute("""
                CREATE TABLE IF NOT EXISTS cells (
                    cell_id BIGINT AUTO_INCREMENT PRIMARY KEY,
                    file_id INT NOT NULL,
                    sheet_name VARCHAR(255),
                    row_num INT,
                    col_num INT,
                    cell_location VARCHAR(20),
                    value TEXT,
                    value_lower TEXT,
                    is_merged BOOLEAN DEFAULT FALSE,
                    merged_range VARCHAR(50),
                    FOREIGN KEY (file_id) REFERENCES files(file_id) ON DELETE CASCADE,
                    INDEX idx_file_id (file_id),
                    INDEX idx_value_lower (value_lower(500)),
                    INDEX idx_sheet (sheet_name),
                    INDEX idx_location (row_num, col_num),
                    FULLTEXT INDEX idx_fulltext (value)
                ) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci
            """)

            self.connection.commit()
            print("✅ 資料表建立成功")
            return True

        except Error as e:
            print(f"❌ 建立資料表失敗: {e}")
            self.connection.rollback()
            return False

    def add_file(self, file_path, file_name, last_modified, file_size):
        """新增檔案記錄"""
        try:
            sql = """
                INSERT INTO files (file_path, file_name, last_modified, file_size)
                VALUES (%s, %s, %s, %s)
                ON DUPLICATE KEY UPDATE
                    last_modified = VALUES(last_modified),
                    file_size = VALUES(file_size),
                    indexed_at = CURRENT_TIMESTAMP
            """
            self.cursor.execute(sql, (file_path, file_name, last_modified, file_size))
            self.connection.commit()
            return self.cursor.lastrowid or self.get_file_id(file_path)
        except Error as e:
            print(f"❌ 新增檔案記錄失敗: {e}")
            self.connection.rollback()
            return None

    def get_file_id(self, file_path):
        """根據路徑獲取檔案 ID"""
        try:
            self.cursor.execute("SELECT file_id FROM files WHERE file_path = %s", (file_path,))
            result = self.cursor.fetchone()
            return result['file_id'] if result else None
        except Error as e:
            print(f"❌ 獲取檔案 ID 失敗: {e}")
            return None

    def get_file_by_path(self, file_path):
        """根據路徑獲取完整檔案資訊"""
        try:
            self.cursor.execute("""
                SELECT file_id, file_path, file_name, last_modified,
                       file_size, cell_count, indexed_at
                FROM files
                WHERE file_path = %s
            """, (file_path,))
            return self.cursor.fetchone()
        except Error as e:
            print(f"❌ 獲取檔案資訊失敗: {e}")
            return None

    def add_cells_batch(self, cells_data):
        """批次新增單元格資料"""
        if not cells_data:
            return 0

        try:
            sql = """
                INSERT INTO cells
                (file_id, sheet_name, row_num, col_num, cell_location, value, value_lower, is_merged, merged_range)
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
            """
            self.cursor.executemany(sql, cells_data)
            self.connection.commit()
            return self.cursor.rowcount
        except Error as e:
            print(f"❌ 批次新增單元格失敗: {e}")
            self.connection.rollback()
            return 0

    def update_file_cell_count(self, file_id, cell_count):
        """更新檔案的單元格數量"""
        try:
            self.cursor.execute(
                "UPDATE files SET cell_count = %s WHERE file_id = %s",
                (cell_count, file_id)
            )
            self.connection.commit()
            return True
        except Error as e:
            print(f"❌ 更新單元格數量失敗: {e}")
            self.connection.rollback()
            return False

    def search(self, keyword, limit=20):
        """搜索單元格內容"""
        try:
            sql = """
                SELECT
                    f.file_name,
                    f.file_path,
                    c.sheet_name,
                    c.cell_location,
                    c.value,
                    c.row_num,
                    c.col_num,
                    c.file_id
                FROM cells c
                JOIN files f ON c.file_id = f.file_id
                WHERE c.value_lower LIKE %s
                ORDER BY f.file_name, c.sheet_name, c.row_num, c.col_num
                LIMIT %s
            """
            search_pattern = f'%{keyword.lower()}%'
            self.cursor.execute(sql, (search_pattern, limit))
            return self.cursor.fetchall()
        except Error as e:
            print(f"❌ 搜索失敗: {e}")
            return []

    def get_stats(self):
        """獲取資料庫統計資訊"""
        try:
            stats = {}

            # 檔案總數
            self.cursor.execute("SELECT COUNT(*) as count FROM files")
            stats['file_count'] = self.cursor.fetchone()['count']

            # 單元格總數
            self.cursor.execute("SELECT COUNT(*) as count FROM cells")
            stats['cell_count'] = self.cursor.fetchone()['count']

            # 最近索引的檔案
            self.cursor.execute("""
                SELECT file_name, file_path, cell_count, indexed_at
                FROM files
                ORDER BY indexed_at DESC
                LIMIT 10
            """)
            stats['recent_files'] = self.cursor.fetchall()

            # 資料庫大小
            self.cursor.execute("""
                SELECT
                    SUM(data_length + index_length) / 1024 / 1024 AS size_mb
                FROM information_schema.TABLES
                WHERE table_schema = %s
            """, (DB_CONFIG['database'],))
            result = self.cursor.fetchone()
            stats['db_size_mb'] = round(result['size_mb'], 2) if result['size_mb'] else 0

            return stats
        except Error as e:
            print(f"❌ 獲取統計資訊失敗: {e}")
            return {}

    def clear_database(self):
        """清空資料庫"""
        try:
            self.cursor.execute("DELETE FROM cells")
            self.cursor.execute("DELETE FROM files")
            self.connection.commit()
            print("✅ 資料庫已清空")
            return True
        except Error as e:
            print(f"❌ 清空資料庫失敗: {e}")
            self.connection.rollback()
            return False

    def delete_file(self, file_path):
        """刪除檔案及其所有單元格"""
        try:
            file_id = self.get_file_id(file_path)
            if file_id:
                # 由於設定了 ON DELETE CASCADE，刪除 files 會自動刪除相關 cells
                self.cursor.execute("DELETE FROM files WHERE file_id = %s", (file_id,))
                self.connection.commit()
                return True
            return False
        except Error as e:
            print(f"❌ 刪除檔案失敗: {e}")
            self.connection.rollback()
            return False

    def get_files_under_path(self, base_path):
        """取得指定路徑下所有已索引的檔案"""
        try:
            # 使用 LIKE 查詢所有以 base_path 開頭的檔案
            sql = """
                SELECT file_id, file_path, file_name, cell_count
                FROM files
                WHERE file_path LIKE %s
            """
            search_pattern = f'{base_path}%'
            self.cursor.execute(sql, (search_pattern,))
            return self.cursor.fetchall()
        except Error as e:
            print(f"❌ 查詢檔案列表失敗: {e}")
            return []


def init_database():
    """初始化資料庫（建立表）"""
    with DatabaseManager() as db:
        if db.connection:
            return db.create_tables()
    return False


if __name__ == '__main__':
    print("=" * 70)
    print("  🗄️  MariaDB 資料庫初始化")
    print("=" * 70)
    print()

    if init_database():
        print()
        print("✅ 資料庫初始化完成！")
        print()
        print("資料表:")
        print("  - files: 儲存 Excel 檔案資訊")
        print("  - cells: 儲存單元格內容")
    else:
        print()
        print("❌ 資料庫初始化失敗")
