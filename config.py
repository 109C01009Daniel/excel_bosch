"""
Excel 搜索系統 - 配置文件
"""
import os

# ============================================================================
# 專案路徑配置
# ============================================================================

# 專案根目錄
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# 數據庫路徑
DATABASE_PATH = os.path.join(BASE_DIR, 'excel_search.db')

# 日志路徑
LOG_DIR = os.path.join(BASE_DIR, 'logs')
LOG_FILE = os.path.join(LOG_DIR, 'excel_search.log')


# ============================================================================
# 索引配置
# ============================================================================

INDEX_CONFIG = {
    # 批量處理配置
    'batch_size': 1000,              # 每批插入的單元格數量
    'max_workers': 4,                # 多線程索引的線程數（階段 4 使用）

    # 文件處理配置
    'skip_empty_cells': True,        # 跳過空白單元格
    'max_cell_length': 10000,        # 單元格最大長度（字符數，避免超大內容）
    'skip_hidden_sheets': False,     # 是否跳過隱藏工作表

    # 合併儲存格配置
    'expand_merged_cells': True,     # 是否展開合併儲存格
    'mark_merged_cells': True,       # 是否標記合併儲存格
}


# ============================================================================
# 支持的文件格式
# ============================================================================

SUPPORTED_EXTENSIONS = ['.xlsx', '.xls']


# ============================================================================
# 搜索配置
# ============================================================================

SEARCH_CONFIG = {
    'default_limit': 100,            # 默認返回結果數
    'max_limit': 1000,               # 最大返回結果數
    'context_length': 100,           # 上下文字符數
    'highlight_keyword': True,       # 是否高亮關鍵詞

    # 緩存配置（階段 4 使用）
    'enable_cache': False,           # 是否啟用緩存
    'cache_size': 1000,              # 緩存大小（查詢數量）
    'cache_ttl_seconds': 600,        # 緩存過期時間（秒）
}


# ============================================================================
# Web 應用配置
# ============================================================================

WEB_CONFIG = {
    'host': '0.0.0.0',               # 監聽地址
    'port': 5000,                    # 監聽端口
    'debug': True,                   # 調試模式
    'threaded': True,                # 多線程模式
}


# ============================================================================
# 日志配置
# ============================================================================

LOGGING_CONFIG = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'standard': {
            'format': '%(asctime)s [%(levelname)s] %(name)s: %(message)s',
            'datefmt': '%Y-%m-%d %H:%M:%S',
        },
        'detailed': {
            'format': '%(asctime)s [%(levelname)s] %(name)s:%(lineno)d: %(message)s',
            'datefmt': '%Y-%m-%d %H:%M:%S',
        },
    },
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
            'level': 'INFO',
            'formatter': 'standard',
            'stream': 'ext://sys.stdout',
        },
        'file': {
            'class': 'logging.handlers.RotatingFileHandler',
            'level': 'DEBUG',
            'formatter': 'detailed',
            'filename': LOG_FILE,
            'maxBytes': 10485760,  # 10MB
            'backupCount': 5,
            'encoding': 'utf8',
        },
    },
    'loggers': {
        '': {  # root logger
            'handlers': ['console', 'file'],
            'level': 'INFO',
            'propagate': True,
        },
    },
}


# ============================================================================
# 數據庫配置
# ============================================================================

DATABASE_CONFIG = {
    # SQLite 優化配置
    'pragma_settings': {
        'journal_mode': 'WAL',        # Write-Ahead Logging（提升並發性能）
        'synchronous': 'NORMAL',      # 平衡性能和安全性
        'cache_size': -64000,         # 64MB 緩存（負數表示 KB）
        'temp_store': 'MEMORY',       # 臨時表存在內存
        'mmap_size': 30000000000,     # 30GB 內存映射（如果支持）
    },

    # 批量操作配置
    'batch_commit_size': 100,         # 每處理多少個文件提交一次
}


# ============================================================================
# 性能監控配置
# ============================================================================

PERFORMANCE_CONFIG = {
    'enable_profiling': False,        # 是否啟用性能分析
    'enable_memory_tracking': False,  # 是否啟用內存追蹤
    'log_slow_queries': True,         # 是否記錄慢查詢
    'slow_query_threshold': 1.0,      # 慢查詢閾值（秒）
}


# ============================================================================
# 輔助函數
# ============================================================================

def ensure_dirs():
    """確保必要的目錄存在"""
    os.makedirs(LOG_DIR, exist_ok=True)


def get_db_size_mb():
    """獲取數據庫大小（MB）"""
    if os.path.exists(DATABASE_PATH):
        size_bytes = os.path.getsize(DATABASE_PATH)
        return round(size_bytes / (1024 * 1024), 2)
    return 0


# 初始化時創建必要目錄
ensure_dirs()
