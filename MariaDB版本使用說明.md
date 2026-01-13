# Excel 搜索系統 - MariaDB 版本使用說明

## 📦 已完成的檔案

```
excel_Bosch/
├── config_mariadb.py              # MariaDB 配置檔
├── database_mariadb.py            # MariaDB 資料庫操作模組
└── excel_search_cli_mariadb.py    # MariaDB CLI 工具
```

---

## 🔧 資料庫配置

### 連接資訊
```python
主機: localhost
Port: 3306
帳號: root
密碼: cctai2025
資料庫: excel_search
Socket: /run/mysqld/mysqld.sock
版本: MariaDB 10.11.13
```

### 資料表結構

#### files 表
```sql
CREATE TABLE files (
    file_id INT AUTO_INCREMENT PRIMARY KEY,
    file_path VARCHAR(1000) NOT NULL UNIQUE,
    file_name VARCHAR(500) NOT NULL,
    last_modified DATETIME,
    file_size BIGINT,
    cell_count INT DEFAULT 0,
    indexed_at DATETIME DEFAULT CURRENT_TIMESTAMP
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4
```

#### cells 表
```sql
CREATE TABLE cells (
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
    FULLTEXT INDEX idx_fulltext (value)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4
```

---

## 🚀 使用方法

### 1. 初始化資料庫

```bash
# 建立資料表（首次使用）
python3 database_mariadb.py
```

輸出：
```
======================================================================
  🗄️  MariaDB 資料庫初始化
======================================================================

✅ 資料表建立成功

✅ 資料庫初始化完成！

資料表:
  - files: 儲存 Excel 檔案資訊
  - cells: 儲存單元格內容
```

### 2. 索引 Excel 檔案

```bash
# 索引目錄中的所有 Excel 檔案
python3 excel_search_cli_mariadb.py index <路徑>

# 只索引當前目錄（不遞迴）
python3 excel_search_cli_mariadb.py index <路徑> --no-recursive
```

**範例**：
```bash
python3 excel_search_cli_mariadb.py index "Sharepoint/Hibiscus2 - Documents/06_Purchasing/6.09_Awarding Documents/01_RFQ" --no-recursive
```

**輸出**：
```
======================================================================
  🔍 開始索引 Excel 檔案 (MariaDB)
======================================================================

✅ 找到 6 個 Excel 檔案

索引檔案: 100%|██████████| 6/6 [00:01<00:00,  3.17file/s]

──────────────────────────────────────────────────────────────────────
✅ 索引完成！成功: 5, 失敗: 1
ℹ️  總共索引 2,660 個單元格
──────────────────────────────────────────────────────────────────────
```

### 3. 搜索內容

```bash
# 基本搜索
python3 excel_search_cli_mariadb.py search "關鍵詞"

# 限制結果數量
python3 excel_search_cli_mariadb.py search "關鍵詞" --limit 10

# 顯示完整內容
python3 excel_search_cli_mariadb.py search "關鍵詞" --full-row
```

**範例**：
```bash
python3 excel_search_cli_mariadb.py search "IR LED" --limit 5
```

**輸出**：
```
======================================================================
  🔍 搜索: "IR LED" (MariaDB)
======================================================================

✅ 找到 5 個結果

──────────────────────────────────────────────────────────────────────
結果 1
📄 檔案: 5.12 Grand Master Test ODM Plan Hibiscus 2 V1.1.xlsx
📊 工作表: EE test
📍 位置: C20 (第20行, 第3列)
📝 內容: IR function
- IR LED
- ICR
- ALS
──────────────────────────────────────────────────────────────────────

ℹ️  查詢時間: 2.33 ms
```

### 4. 查看統計資訊

```bash
python3 excel_search_cli_mariadb.py stats
```

**輸出**：
```
======================================================================
  📊 資料庫統計 (MariaDB)
======================================================================

📁 檔案總數: 5
📊 單元格總數: 2,660
💾 資料庫大小: 1.19 MB
🔗 資料庫: excel_search
🖥️  主機: localhost:3306

最近索引的檔案 (前 10 個):

  1. 5.18 8D Report & Problem Solving Sheet.xlsx
     📍 路徑: /var/www/html/excel_Bosch/Sharepoint/...
     📊 單元格: 863 | 索引時間: 2026-01-07 16:24:04
```

### 5. 清空資料庫

```bash
python3 excel_search_cli_mariadb.py clear
```

**確認提示**：
```
確定要清空整個資料庫嗎？ [y/N]: y
```

### 6. 系統資訊

```bash
python3 excel_search_cli_mariadb.py info
```

---

## 🔍 搜索特性

### 1. 不區分大小寫
```bash
搜索 "LED" = "led" = "Led"
```

### 2. 部分匹配
```bash
搜索 "LED" 會找到：
  - "IR LED"
  - "LED driver"
  - "OLED"
```

### 3. 搜索所有工作表
自動搜索所有工作表，包括：
- CheckList
- GPIO
- RevisionHistory
- 等等...

### 4. 精確位置
每個結果包含：
- 檔案名稱和路徑
- 工作表名稱
- 單元格位置（如 C58）
- 行號和列號
- 單元格內容

---

## 📊 效能比較

### 測試資料
```
檔案數: 5 個
單元格數: 2,660 個
資料庫大小: 1.19 MB
```

### MariaDB vs SQLite

| 項目 | MariaDB | SQLite |
|------|---------|--------|
| 搜索時間 | 2.33 ms | 0.57 ms |
| 資料庫大小 | 1.19 MB | 1.0 MB |
| 索引時間 | ~1.5 秒 | ~0.5 秒 |
| 記憶體使用 | 326.7 MB (伺服器) | 幾 MB |
| 連接方式 | TCP/Socket | 直接開檔 |

**結論**：
- SQLite 稍快（本地小資料量）
- MariaDB 適合多人使用、大量資料
- 目前資料量下兩者差異不大

---

## 🛠️ 直接操作 MariaDB

### 連接資料庫
```bash
mysql -u root -pcctai2025 --socket=/run/mysqld/mysqld.sock excel_search
```

### 常用查詢

**查看所有表**：
```sql
SHOW TABLES;
```

**查看表結構**：
```sql
DESCRIBE files;
DESCRIBE cells;
```

**統計資料**：
```sql
-- 檔案總數
SELECT COUNT(*) FROM files;

-- 單元格總數
SELECT COUNT(*) FROM cells;

-- 每個檔案的單元格數
SELECT f.file_name, COUNT(*) as cell_count
FROM cells c
JOIN files f ON c.file_id = f.file_id
GROUP BY f.file_name
ORDER BY cell_count DESC;
```

**搜索內容**：
```sql
-- 基本搜索
SELECT f.file_name, c.sheet_name, c.cell_location, c.value
FROM cells c
JOIN files f ON c.file_id = f.file_id
WHERE c.value_lower LIKE '%ir led%'
LIMIT 10;

-- 使用全文索引（更快）
SELECT f.file_name, c.sheet_name, c.cell_location, c.value
FROM cells c
JOIN files f ON c.file_id = f.file_id
WHERE MATCH(c.value) AGAINST('IR LED')
LIMIT 10;
```

**資料庫大小**：
```sql
SELECT
    table_name,
    ROUND(data_length / 1024 / 1024, 2) AS data_mb,
    ROUND(index_length / 1024 / 1024, 2) AS index_mb,
    ROUND((data_length + index_length) / 1024 / 1024, 2) AS total_mb
FROM information_schema.TABLES
WHERE table_schema = 'excel_search';
```

---

## ⚡ 進階功能

### 1. 批次插入優化

config_mariadb.py 中設定：
```python
BATCH_SIZE = 1000  # 每次插入 1000 筆
```

### 2. 索引優化

已建立的索引：
- `idx_file_id`: 加速 JOIN 操作
- `idx_value_lower`: 加速內容搜索 ⭐
- `idx_sheet`: 加速工作表篩選
- `idx_fulltext`: 全文搜索索引

### 3. 外鍵約束

```sql
FOREIGN KEY (file_id) REFERENCES files(file_id) ON DELETE CASCADE
```

刪除檔案時自動刪除相關單元格。

---

## 🔧 故障排除

### 問題 1: 連接失敗
```
ERROR 2002 (HY000): Can't connect to local MySQL server
```

**解決方法**：
```bash
# 檢查 MariaDB 是否運行
systemctl status mariadb

# 如果沒運行，啟動它
sudo systemctl start mariadb
```

### 問題 2: 權限不足
```
ERROR 1045 (28000): Access denied for user 'root'
```

**解決方法**：
確認 config_mariadb.py 中的密碼正確。

### 問題 3: 資料庫不存在
```
ERROR 1049 (42000): Unknown database 'excel_search'
```

**解決方法**：
```bash
mysql -u root -pcctai2025 --socket=/run/mysqld/mysqld.sock -e "CREATE DATABASE excel_search CHARACTER SET utf8mb4"
```

### 問題 4: .xls 格式不支援
```
openpyxl does not support the old .xls file format
```

**解決方法**：
舊格式 .xls 檔案會被跳過。可以手動轉換成 .xlsx 格式。

---

## 📚 與 SQLite 版本對比

### 相同功能
- ✅ 索引 Excel 檔案
- ✅ 搜索內容
- ✅ 顯示統計資訊
- ✅ 清空資料庫
- ✅ CLI 介面

### 主要差異

| 特性 | SQLite 版本 | MariaDB 版本 |
|------|------------|-------------|
| 檔案 | excel_search_cli.py | excel_search_cli_mariadb.py |
| 配置 | config.py | config_mariadb.py |
| 資料庫 | database.py | database_mariadb.py |
| 儲存 | excel_search.db 檔案 | MariaDB 伺服器 |
| 連接 | 直接開檔 | TCP/Socket 連接 |
| 依賴 | 內建 sqlite3 | mysql-connector-python |
| FTS | FTS5 (未使用) | FULLTEXT (已建立) |
| 佔位符 | ? | %s |
| 自增 | AUTOINCREMENT | AUTO_INCREMENT |

---

## 🎯 建議使用場景

### 使用 MariaDB 版本當：
- ✅ 需要多人同時訪問
- ✅ 資料量超過 1GB
- ✅ 需要遠端訪問
- ✅ 需要複雜權限管理
- ✅ 已有 MariaDB 環境

### 使用 SQLite 版本當：
- ✅ 單人使用
- ✅ 資料量 < 1GB
- ✅ 本機使用
- ✅ 需要輕量級方案
- ✅ 需要簡單移植

---

## 📝 測試結果

### 已測試功能
✅ 資料庫連接
✅ 資料表建立
✅ 檔案索引（5 個檔案）
✅ 內容搜索（找到 5 個結果）
✅ 統計資訊顯示
✅ 中文支援（utf8mb4）

### 測試資料
```
索引檔案: 5 個
單元格數: 2,660 個
搜索測試: "IR LED" (5 個結果)
查詢時間: 2.33 ms
資料庫大小: 1.19 MB
```

---

## 🔄 下一步建議

1. **索引更多檔案**
```bash
python3 excel_search_cli_mariadb.py index ./Sharepoint
```

2. **建立 Web 介面**
修改 database_viewer.py 支援 MariaDB

3. **效能優化**
- 啟用查詢快取
- 調整 InnoDB buffer pool
- 使用 FULLTEXT 索引

4. **備份策略**
```bash
mysqldump -u root -pcctai2025 excel_search > backup.sql
```

---

**版本**: 1.0.0
**建立日期**: 2026-01-07
**資料庫**: MariaDB 10.11.13
**Python**: 3.11
