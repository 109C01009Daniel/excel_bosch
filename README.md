# Excel 搜索系統

一個快速搜索大量 Excel 文件內容的工具系統。

## 🌟 特性

- ✅ 支持 .xlsx 和 .xls 格式
- ✅ 全文索引，秒級搜索
- ✅ 支持合併儲存格
- ✅ 命令行和 Web 界面
- ✅ 支持 500-1000 個 Excel 文件
- ✅ 多種搜索模式（精確匹配、部分匹配、不區分大小寫）
- ✅ 返回完整行數據
- ✅ 導出搜索結果為 CSV

## 📋 系統需求

- Python 3.8+
- SQLite 3.9+（支持 FTS5）
- 2GB+ RAM（建議 4GB+）
- 5GB+ 可用磁盤空間

## 🚀 快速開始

### 1. 安裝依賴

```bash
pip install -r requirements.txt
```

### 2. 索引 Excel 文件

```bash
python cli.py index /path/to/your/excel/folder
```

### 3. 搜索

```bash
python cli.py search "PN3004"
```

### 4. 啟動 Web 界面（開發中）

```bash
python web_app.py
```

訪問：http://localhost:5000

## 📂 專案結構

```
excel_Bosch/
├── config.py                 # 配置文件
├── database.py              # 數據庫模組
├── excel_reader.py          # Excel 讀取器
├── merged_cells_handler.py  # 合併儲存格處理
├── indexer.py               # 索引器
├── searcher.py              # 搜索引擎
├── cli.py                   # 命令行工具
├── web_app.py               # Web 應用
├── requirements.txt         # 依賴包
├── README.md                # 本文件
├── 開發流程/                # 開發文檔
│   └── 開發進度規劃.txt
├── templates/               # Web 模板
├── static/                  # 靜態文件
└── logs/                    # 日志文件
```

## 🎯 開發狀態

當前階段：**階段 1 - 核心基礎建設**

- [x] 1.1 建立專案結構和依賴管理
- [ ] 1.2 實現數據庫模組
- [ ] 1.3 實現 Excel 讀取器
- [ ] 1.4 實現合併儲存格處理
- [ ] 1.5 實現索引器
- [ ] 1.6 實現搜索引擎
- [ ] 1.7 測試核心功能

詳細開發計劃請查看：`開發流程/開發進度規劃.txt`

## 📖 技術架構

### 後端技術
- **數據庫**：SQLite + FTS5（全文索引）
- **Excel 處理**：openpyxl（.xlsx）+ xlrd（.xls）
- **CLI 框架**：Click
- **Web 框架**：Flask

### 核心設計
- **扁平化存儲**：將所有單元格內容提取為文本片段
- **倒排索引**：使用 FTS5 建立關鍵詞到文件的映射
- **批量處理**：每 1000 條記錄批量插入，提升性能
- **增量更新**：只重新索引修改過的文件

### 數據庫結構
- `files` 表：文件元數據
- `cells` 表：單元格詳細信息
- `content_fts` 表：FTS5 全文索引

## 📊 性能指標（預期）

| 指標 | 目標值 |
|------|--------|
| 索引速度 | 1000 文件 < 15 分鐘 |
| 搜索速度 | < 2 秒 |
| 數據庫大小 | ~2-3 GB（1000 文件） |
| 並發用戶 | 10+ |

## 🤝 貢獻

歡迎提交 Issue 和 Pull Request！

## 📄 授權

MIT License

## 📧 聯繫

如有問題，請提交 Issue。
# excel_bosch
