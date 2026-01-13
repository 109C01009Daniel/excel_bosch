# MariaDB 版本 - 指令快速參考

## 🚀 最常用指令（必記）

```bash
# 1. 增量索引（日常使用，推薦）
python3 excel_search_cli_mariadb.py index "Sharepoint"

# 2. 搜索內容
python3 excel_search_cli_mariadb.py search "關鍵詞"

# 3. 查看統計
python3 excel_search_cli_mariadb.py stats
```

---

## 📥 索引指令完整說明

### 基本索引

```bash
# 增量索引（預設，推薦）⭐
python3 excel_search_cli_mariadb.py index "Sharepoint"

# 等同於
python3 excel_search_cli_mariadb.py index "Sharepoint" --incremental
```

### 索引模式選擇

```bash
# 增量索引（只處理變動檔案）⭐ 推薦
python3 excel_search_cli_mariadb.py index "Sharepoint" --incremental

# 全量重新索引（處理所有檔案）
python3 excel_search_cli_mariadb.py index "Sharepoint" --full
```

### 遞迴選項

```bash
# 遞迴索引（包含所有子目錄，預設）
python3 excel_search_cli_mariadb.py index "Sharepoint"

# 不遞迴（只索引當前目錄）
python3 excel_search_cli_mariadb.py index "Sharepoint/某目錄" --no-recursive
```

### 結合使用

```bash
# 全量 + 不遞迴
python3 excel_search_cli_mariadb.py index "路徑" --full --no-recursive
```

---

## 🔍 搜索指令完整說明

### 基本搜索

```bash
# 基本搜索（預設 20 筆）
python3 excel_search_cli_mariadb.py search "關鍵詞"

# 限制結果數量
python3 excel_search_cli_mariadb.py search "關鍵詞" --limit 5
python3 excel_search_cli_mariadb.py search "關鍵詞" --limit 100

# 顯示完整內容（不截斷）
python3 excel_search_cli_mariadb.py search "關鍵詞" --full-row

# 結合使用
python3 excel_search_cli_mariadb.py search "關鍵詞" --limit 10 --full-row
```

### 各種搜索類型

```bash
# 英文搜索（不區分大小寫）
python3 excel_search_cli_mariadb.py search "driver"
python3 excel_search_cli_mariadb.py search "Driver"
python3 excel_search_cli_mariadb.py search "DRIVER"
# 以上三個結果相同

# 中文搜索
python3 excel_search_cli_mariadb.py search "鏡頭"

# 數字搜索
python3 excel_search_cli_mariadb.py search "12345"

# 特殊字元（需要引號）
python3 excel_search_cli_mariadb.py search "IR-LED-001"
python3 excel_search_cli_mariadb.py search "test@example.com"
```

---

## 📊 統計與資訊指令

```bash
# 查看資料庫統計
python3 excel_search_cli_mariadb.py stats

# 查看系統資訊
python3 excel_search_cli_mariadb.py info
```

---

## 🗑️ 資料庫管理指令

```bash
# 清空資料庫（會要求確認）
python3 excel_search_cli_mariadb.py clear

# 自動確認清空（自動化腳本用）
yes | python3 excel_search_cli_mariadb.py clear
```

---

## 🎯 各種場景實際操作

### 場景 1：我有新增檔案

```bash
# 步驟 1：複製或新增檔案到目錄
cp 新檔案.xlsx Sharepoint/

# 步驟 2：執行增量索引（會自動偵測新檔案）
python3 excel_search_cli_mariadb.py index "Sharepoint"

# 步驟 3：確認索引成功
python3 excel_search_cli_mariadb.py stats

# 步驟 4：搜索新檔案內容
python3 excel_search_cli_mariadb.py search "新檔案中的關鍵字"
```

**預期輸出：**
```
➕ 新增檔案: 1
⏭️  跳過檔案: 186
```

---

### 場景 2：我修改了檔案內容

```bash
# 步驟 1：修改檔案（用 Excel、LibreOffice 等）
# （手動編輯並儲存）

# 步驟 2：執行增量索引（會自動偵測修改）
python3 excel_search_cli_mariadb.py index "Sharepoint"

# 步驟 3：搜索修改後的內容
python3 excel_search_cli_mariadb.py search "修改後的關鍵字"
```

**預期輸出：**
```
🔄 更新檔案: 1
⏭️  跳過檔案: 186
```

---

### 場景 3：我刪除了檔案

```bash
# 步驟 1：刪除檔案
rm Sharepoint/要刪除的檔案.xlsx

# 步驟 2：執行增量索引（會自動清理）
python3 excel_search_cli_mariadb.py index "Sharepoint"

# 步驟 3：確認已清理
python3 excel_search_cli_mariadb.py stats
```

**預期輸出：**
```
🔍 檢查已刪除的檔案...
🗑️  清除: 要刪除的檔案.xlsx (已刪除)
🗑️  清除檔案: 1
```

---

### 場景 4：檔案沒有變動（效能測試）

```bash
# 不做任何修改，直接執行增量索引
python3 excel_search_cli_mariadb.py index "Sharepoint"
```

**預期輸出：**
```
⏭️  跳過檔案: 187
（完成時間：< 1 秒）
```

---

### 場景 5：首次建立索引

```bash
# 選項 A：使用增量索引（推薦）
python3 excel_search_cli_mariadb.py index "Sharepoint"

# 選項 B：使用全量索引
python3 excel_search_cli_mariadb.py index "Sharepoint" --full

# 兩者首次執行結果相同，但增量索引是推薦做法
```

---

### 場景 6：完全重建索引

```bash
# 步驟 1：清空資料庫
python3 excel_search_cli_mariadb.py clear

# 步驟 2：全量重新索引
python3 excel_search_cli_mariadb.py index "Sharepoint" --full

# 步驟 3：確認索引結果
python3 excel_search_cli_mariadb.py stats
```

---

## ⚡ 效能比較

### 測試資料（332 個檔案）

| 索引模式 | 執行時間 | 使用情境 |
|---------|---------|---------|
| **增量索引** | 0.236 秒 ⚡ | 日常使用（推薦） |
| **全量索引** | 238 秒 | 首次建立或完全重建 |
| **提升倍數** | **1,008 倍** | - |

### 實際測量

```bash
# 測量增量索引時間
time python3 excel_search_cli_mariadb.py index "Sharepoint"

# 測量全量索引時間
time python3 excel_search_cli_mariadb.py index "Sharepoint" --full
```

---

## 🧠 增量索引判斷邏輯

### 判斷依據

```
比對層級：檔案級別（不是儲存格級別）
比對依據：檔案系統的 last_modified 時間戳
```

### 判斷流程

```
1. 檔案不存在於資料庫
   → ➕ 判定：新增檔案
   → 動作：直接索引

2. 檔案存在，時間戳相同或更舊
   → ⏭️  判定：未變動
   → 動作：跳過處理

3. 檔案存在，時間戳變新
   → 🔄 判定：已修改
   → 動作：刪除舊資料 → 重新索引

4. 資料庫有檔案，但檔案系統找不到
   → 🗑️  判定：已刪除
   → 動作：清除資料庫記錄（CASCADE 自動刪除相關儲存格）
```

---

## 🔧 實用組合指令

### 索引後查看統計

```bash
python3 excel_search_cli_mariadb.py index "Sharepoint" && \
python3 excel_search_cli_mariadb.py stats
```

### 清空後重建

```bash
python3 excel_search_cli_mariadb.py clear && \
python3 excel_search_cli_mariadb.py index "Sharepoint" --full
```

### 批次搜索多個關鍵字

```bash
for keyword in "test" "driver" "LED"; do
    echo "搜索: $keyword"
    python3 excel_search_cli_mariadb.py search "$keyword" --limit 5
    echo ""
done
```

### 儲存搜索結果

```bash
# 儲存到檔案
python3 excel_search_cli_mariadb.py search "關鍵詞" > 搜索結果.txt

# 儲存統計資訊
python3 excel_search_cli_mariadb.py stats > 資料庫統計.txt
```

---

## 📋 完整參數表

### index 指令

| 參數 | 預設值 | 說明 |
|-----|-------|------|
| `<路徑>` | 必填 | 要索引的目錄路徑 |
| `--recursive` | ✅ 啟用 | 遞迴索引子目錄 |
| `--no-recursive` | ❌ 關閉 | 只索引當前目錄 |
| `--incremental` | ✅ 啟用 | 增量索引（只處理變動） |
| `--full` | ❌ 關閉 | 全量重新索引 |

### search 指令

| 參數 | 預設值 | 說明 |
|-----|-------|------|
| `<關鍵詞>` | 必填 | 要搜索的關鍵字 |
| `--limit` | 20 | 結果數量限制 |
| `--full-row` | ❌ 關閉 | 顯示完整內容（不截斷） |

---

## ❓ 常見問題快速解答

**Q: 我有新增檔案，要用什麼指令？**
```bash
python3 excel_search_cli_mariadb.py index "Sharepoint"
```

**Q: 我修改了檔案，需要重新索引嗎？**
```bash
# 是的，執行增量索引即可自動偵測修改
python3 excel_search_cli_mariadb.py index "Sharepoint"
```

**Q: 搜索結果太多怎麼辦？**
```bash
python3 excel_search_cli_mariadb.py search "關鍵詞" --limit 5
```

**Q: 內容被截斷看不完整？**
```bash
python3 excel_search_cli_mariadb.py search "關鍵詞" --full-row
```

**Q: 每天都要重新索引嗎？**
```bash
# 建議定期執行增量索引（速度很快）
python3 excel_search_cli_mariadb.py index "Sharepoint"
```

**Q: 什麼時候用全量索引？**
```bash
# 只有以下情況需要：
# 1. 首次建立索引
# 2. 懷疑資料庫損壞
# 3. 完全重建索引
python3 excel_search_cli_mariadb.py index "Sharepoint" --full
```

---

## 🎯 建議使用方式

### 日常使用（推薦）

```bash
# 每天或每週執行一次
python3 excel_search_cli_mariadb.py index "Sharepoint"

# 隨時搜索
python3 excel_search_cli_mariadb.py search "你的關鍵字"
```

### 首次設定

```bash
# 第一次使用
python3 excel_search_cli_mariadb.py index "Sharepoint"
python3 excel_search_cli_mariadb.py stats
```

### 定期維護

```bash
# 每週檢查統計
python3 excel_search_cli_mariadb.py stats

# 如有異常，重建索引
python3 excel_search_cli_mariadb.py clear
python3 excel_search_cli_mariadb.py index "Sharepoint" --full
```

---

## 📚 相關文件

- **完整使用說明**：`MariaDB版本使用說明.md`
- **測試腳本**：`quick_test_mariadb.sh`
- **工作日誌**：`每日進度/工作日誌_2026-01-08.md`
- **資料庫配置**：`config_mariadb.py`

---

## 🚀 快速開始（3 步驟）

```bash
# 1. 索引檔案
python3 excel_search_cli_mariadb.py index "Sharepoint"

# 2. 搜索內容
python3 excel_search_cli_mariadb.py search "你的關鍵字"

# 3. 查看統計
python3 excel_search_cli_mariadb.py stats
```

就這麼簡單！🎉
