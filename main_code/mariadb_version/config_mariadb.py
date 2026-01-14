#!/usr/bin/env python3
"""
MariaDB 配置檔
Excel 搜索系統 - MariaDB 版本
"""
import os

# 工作目錄
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# MariaDB 連線設定
DB_CONFIG = {
    'host': 'localhost',
    'port': 3306,
    'user': 'root',
    'password': 'cctai2025',
    'database': 'excel_search',
    'charset': 'utf8mb4',
    'unix_socket': '/run/mysqld/mysqld.sock',  # 指定 socket 路徑
    'autocommit': False,
    'use_unicode': True,
    'collation': 'utf8mb4_unicode_ci'
}

# Excel 檔案搜索設定
EXCEL_EXTENSIONS = ['.xlsx', '.xlsm', '.xls']
IGNORE_PATTERNS = ['~$*', '.*']  # 忽略暫存檔和隱藏檔
MIN_FILE_SIZE = 1024  # 最小檔案大小 (bytes)

# 索引設定
BATCH_SIZE = 1000  # 批次插入大小
MAX_CELL_LENGTH = 10000  # 單元格最大長度

# 顯示設定
DEFAULT_SEARCH_LIMIT = 20  # 預設搜索結果數量
MAX_SEARCH_LIMIT = 1000  # 最大搜索結果數量
