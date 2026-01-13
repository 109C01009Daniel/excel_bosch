"""
Excel 搜索系統 - 檔案掃描模組
負責掃描目錄中的 Excel 檔案並獲取元數據
"""
import os
import logging
from pathlib import Path
from datetime import datetime
from typing import List, Dict, Any, Optional
from tqdm import tqdm

from config import SUPPORTED_EXTENSIONS

logger = logging.getLogger(__name__)


class FileScanner:
    """
    Excel 檔案掃描器

    負責掃描指定目錄中的所有 Excel 檔案，並獲取檔案的元數據信息。
    """

    def __init__(self,
                 supported_extensions: List[str] = None,
                 exclude_hidden: bool = True,
                 min_size_bytes: int = 0):
        """
        初始化檔案掃描器

        Args:
            supported_extensions: 支援的檔案副檔名列表（例如 ['.xlsx', '.xls']）
            exclude_hidden: 是否排除隱藏檔案（以 . 開頭或在隱藏目錄中）
            min_size_bytes: 最小檔案大小（bytes），小於此大小的檔案將被忽略
        """
        self.supported_extensions = supported_extensions or SUPPORTED_EXTENSIONS
        self.exclude_hidden = exclude_hidden
        self.min_size_bytes = min_size_bytes

        logger.info(f"初始化檔案掃描器: 支援格式={self.supported_extensions}, "
                   f"排除隱藏={self.exclude_hidden}, 最小大小={self.min_size_bytes}B")

    def scan_directory(self,
                      directory: str,
                      recursive: bool = True,
                      show_progress: bool = True) -> List[Dict[str, Any]]:
        """
        掃描目錄中的所有 Excel 檔案

        Args:
            directory: 要掃描的目錄路徑
            recursive: 是否遞迴掃描子目錄
            show_progress: 是否顯示進度條

        Returns:
            List[Dict]: 檔案資訊列表，每個元素包含：
                - file_path: 檔案完整路徑
                - file_name: 檔案名稱
                - file_size: 檔案大小（bytes）
                - last_modified: 最後修改時間
                - extension: 副檔名
                - relative_path: 相對路徑

        Raises:
            FileNotFoundError: 目錄不存在
            PermissionError: 無權限訪問目錄
        """
        # 驗證目錄
        directory = os.path.abspath(directory)
        if not os.path.exists(directory):
            raise FileNotFoundError(f"目錄不存在: {directory}")
        if not os.path.isdir(directory):
            raise NotADirectoryError(f"不是目錄: {directory}")

        logger.info(f"開始掃描目錄: {directory} (遞迴={recursive})")

        # 收集所有檔案路徑
        all_files = []

        if recursive:
            # 遞迴掃描
            for root, dirs, files in os.walk(directory):
                # 排除隱藏目錄
                if self.exclude_hidden:
                    dirs[:] = [d for d in dirs if not d.startswith('.')]

                for filename in files:
                    file_path = os.path.join(root, filename)
                    if self._should_include(file_path, filename):
                        all_files.append(file_path)
        else:
            # 只掃描當前目錄
            try:
                for filename in os.listdir(directory):
                    file_path = os.path.join(directory, filename)
                    if os.path.isfile(file_path) and self._should_include(file_path, filename):
                        all_files.append(file_path)
            except PermissionError as e:
                logger.error(f"無權限訪問目錄: {directory}")
                raise

        logger.info(f"找到 {len(all_files)} 個 Excel 檔案")

        # 獲取每個檔案的詳細資訊
        file_infos = []

        if show_progress and len(all_files) > 0:
            # 使用進度條
            for file_path in tqdm(all_files, desc="掃描檔案", unit="個"):
                try:
                    info = self.get_file_info(file_path, base_dir=directory)
                    if info:
                        file_infos.append(info)
                except Exception as e:
                    logger.warning(f"無法讀取檔案資訊: {file_path}, 錯誤: {e}")
        else:
            # 不顯示進度條
            for file_path in all_files:
                try:
                    info = self.get_file_info(file_path, base_dir=directory)
                    if info:
                        file_infos.append(info)
                except Exception as e:
                    logger.warning(f"無法讀取檔案資訊: {file_path}, 錯誤: {e}")

        # 按修改時間排序（最新的在前）
        file_infos.sort(key=lambda x: x['last_modified'], reverse=True)

        logger.info(f"成功掃描 {len(file_infos)} 個檔案")
        return file_infos

    def get_file_info(self, file_path: str, base_dir: str = None) -> Optional[Dict[str, Any]]:
        """
        獲取單個檔案的詳細資訊

        Args:
            file_path: 檔案路徑
            base_dir: 基礎目錄（用於計算相對路徑）

        Returns:
            Dict: 檔案資訊字典，包含：
                - file_path: 絕對路徑
                - file_name: 檔案名稱
                - file_size: 檔案大小（bytes）
                - file_size_mb: 檔案大小（MB）
                - last_modified: 最後修改時間（datetime）
                - extension: 副檔名
                - relative_path: 相對路徑（如果提供 base_dir）

            如果檔案無法訪問，返回 None
        """
        try:
            # 獲取檔案統計資訊
            stat = os.stat(file_path)

            # 獲取絕對路徑
            abs_path = os.path.abspath(file_path)

            # 計算相對路徑
            relative_path = None
            if base_dir:
                try:
                    relative_path = os.path.relpath(abs_path, base_dir)
                except ValueError:
                    # 不同磁碟機，無法計算相對路徑
                    relative_path = abs_path

            # 組裝資訊
            info = {
                'file_path': abs_path,
                'file_name': os.path.basename(file_path),
                'file_size': stat.st_size,
                'file_size_mb': round(stat.st_size / (1024 * 1024), 2),
                'last_modified': datetime.fromtimestamp(stat.st_mtime),
                'extension': os.path.splitext(file_path)[1].lower(),
                'relative_path': relative_path,
            }

            return info

        except (OSError, PermissionError) as e:
            logger.warning(f"無法讀取檔案: {file_path}, 錯誤: {e}")
            return None

    def get_summary(self, file_infos: List[Dict[str, Any]]) -> Dict[str, Any]:
        """
        獲取掃描結果的統計摘要

        Args:
            file_infos: 檔案資訊列表

        Returns:
            Dict: 統計資訊
        """
        if not file_infos:
            return {
                'total_files': 0,
                'total_size_mb': 0,
                'extensions': {},
                'largest_file': None,
                'newest_file': None,
            }

        # 計算統計資訊
        total_size = sum(f['file_size'] for f in file_infos)

        # 按副檔名分組
        extensions = {}
        for info in file_infos:
            ext = info['extension']
            extensions[ext] = extensions.get(ext, 0) + 1

        # 找出最大的檔案
        largest = max(file_infos, key=lambda x: x['file_size'])

        # 找出最新的檔案
        newest = max(file_infos, key=lambda x: x['last_modified'])

        return {
            'total_files': len(file_infos),
            'total_size_mb': round(total_size / (1024 * 1024), 2),
            'extensions': extensions,
            'largest_file': {
                'name': largest['file_name'],
                'size_mb': largest['file_size_mb'],
            },
            'newest_file': {
                'name': newest['file_name'],
                'modified': newest['last_modified'].strftime('%Y-%m-%d %H:%M:%S'),
            },
        }

    # ========================================================================
    # 私有輔助方法
    # ========================================================================

    def _should_include(self, file_path: str, filename: str) -> bool:
        """
        判斷檔案是否應該被包含在掃描結果中

        Args:
            file_path: 檔案路徑
            filename: 檔案名稱

        Returns:
            bool: True 表示應該包含
        """
        # 1. 檢查是否為 Excel 檔案
        if not self._is_excel_file(filename):
            return False

        # 2. 排除隱藏檔案
        if self.exclude_hidden and filename.startswith('.'):
            return False

        # 3. 檢查檔案大小
        try:
            file_size = os.path.getsize(file_path)
            if file_size < self.min_size_bytes:
                logger.debug(f"檔案太小，跳過: {filename} ({file_size} bytes)")
                return False
        except OSError:
            return False

        # 4. 排除臨時檔案（Excel 開啟時會產生 ~$ 開頭的臨時檔）
        if filename.startswith('~$'):
            logger.debug(f"跳過臨時檔案: {filename}")
            return False

        return True

    def _is_excel_file(self, filename: str) -> bool:
        """
        判斷檔案是否為 Excel 檔案

        Args:
            filename: 檔案名稱

        Returns:
            bool: True 表示是 Excel 檔案
        """
        ext = os.path.splitext(filename)[1].lower()
        return ext in self.supported_extensions


# ============================================================================
# 便捷函數（不需要創建 FileScanner 實例）
# ============================================================================

def quick_scan(directory: str,
               recursive: bool = True,
               show_progress: bool = True) -> List[Dict[str, Any]]:
    """
    快速掃描目錄（使用預設配置）

    Args:
        directory: 要掃描的目錄
        recursive: 是否遞迴掃描
        show_progress: 是否顯示進度

    Returns:
        List[Dict]: 檔案資訊列表
    """
    scanner = FileScanner()
    return scanner.scan_directory(directory, recursive, show_progress)


def print_summary(file_infos: List[Dict[str, Any]]):
    """
    列印掃描結果摘要

    Args:
        file_infos: 檔案資訊列表
    """
    scanner = FileScanner()
    summary = scanner.get_summary(file_infos)

    print("\n" + "=" * 60)
    print("📊 掃描結果摘要")
    print("=" * 60)
    print(f"總檔案數:   {summary['total_files']} 個")
    print(f"總大小:     {summary['total_size_mb']} MB")
    print(f"\n檔案格式分佈:")
    for ext, count in summary['extensions'].items():
        percentage = (count / summary['total_files']) * 100
        print(f"  {ext:6s} : {count:4d} 個 ({percentage:.1f}%)")

    if summary['largest_file']:
        print(f"\n最大檔案:   {summary['largest_file']['name']} "
              f"({summary['largest_file']['size_mb']} MB)")

    if summary['newest_file']:
        print(f"最新檔案:   {summary['newest_file']['name']} "
              f"({summary['newest_file']['modified']})")

    print("=" * 60 + "\n")


# ============================================================================
# 測試程式
# ============================================================================

if __name__ == '__main__':
    import logging.config
    from config import LOGGING_CONFIG

    # 配置日誌
    logging.config.dictConfig(LOGGING_CONFIG)

    print("🔍 Excel 檔案掃描器測試\n")

    # 測試掃描當前目錄
    test_dir = input("請輸入要掃描的目錄路徑（按 Enter 使用當前目錄）: ").strip()
    if not test_dir:
        test_dir = '.'

    try:
        # 創建掃描器
        scanner = FileScanner(
            exclude_hidden=True,
            min_size_bytes=1024  # 至少 1KB
        )

        # 掃描目錄
        print(f"\n正在掃描: {os.path.abspath(test_dir)}\n")
        files = scanner.scan_directory(test_dir, recursive=True, show_progress=True)

        # 顯示結果
        if files:
            print(f"\n✅ 找到 {len(files)} 個 Excel 檔案\n")

            # 顯示前 10 個檔案
            print("前 10 個檔案:")
            print("-" * 80)
            for i, file_info in enumerate(files[:10], 1):
                print(f"{i:2d}. {file_info['file_name']}")
                print(f"    路徑: {file_info['relative_path']}")
                print(f"    大小: {file_info['file_size_mb']} MB")
                print(f"    修改: {file_info['last_modified'].strftime('%Y-%m-%d %H:%M:%S')}")
                print()

            if len(files) > 10:
                print(f"... 還有 {len(files) - 10} 個檔案\n")

            # 顯示統計摘要
            print_summary(files)

        else:
            print("❌ 沒有找到 Excel 檔案")

    except FileNotFoundError as e:
        print(f"❌ 錯誤: {e}")
    except PermissionError as e:
        print(f"❌ 權限錯誤: {e}")
    except Exception as e:
        print(f"❌ 未知錯誤: {e}")
        import traceback
        traceback.print_exc()
