# Excel 搜索系統 - CLI 使用指南

## 🚀 快速開始

### 安裝依賴
```bash
pip install -r requirements.txt
```

### 基本使用流程

```bash
# 1. 索引檔案
python3 excel_search_cli.py index <路徑>

# 2. 搜索關鍵詞
python3 excel_search_cli.py search "<關鍵詞>"

# 3. 查看統計
python3 excel_search_cli.py stats
```

---

## 📖 命令詳解

### 1. index - 索引檔案

**索引單個檔案：**
```bash
python3 excel_search_cli.py index "test.xlsx"
```

**索引整個目錄（遞迴）：**
```bash
python3 excel_search_cli.py index "Sharepoint" --recursive
```

**索引目錄（不遞迴）：**
```bash
python3 excel_search_cli.py index "Sharepoint" --no-recursive
```

**輸出範例：**
```
======================================================================
  📚 索引 Excel 檔案
======================================================================

ℹ️  掃描目錄: Sharepoint
✅ 找到 6 個 Excel 檔案

索引中: 100%|██████████| 6/6 [00:00<00:00, 8.55檔案/s, 成功=5, 單元格=2660]

======================================================================
  📊 索引完成
======================================================================

✅ 成功索引: 5 個檔案
⚠️  失敗: 1 個檔案
ℹ️  總單元格數: 2,660
ℹ️  資料庫大小: 1.0 MB
```

---

### 2. search - 搜索關鍵詞

**基本搜索：**
```bash
python3 excel_search_cli.py search "PN3004"
```

**限制結果數量：**
```bash
python3 excel_search_cli.py search "USB" --limit 10
```

**顯示完整行資料：**
```bash
python3 excel_search_cli.py search "product" --full-row
```

**輸出範例：**
```
======================================================================
  🔍 搜索: "product"
======================================================================

✅ 找到 2 個結果

──────────────────────────────────────────────────────────────────────
結果 1
📄 檔案: Start of the art evaluation_Hibiscus2.xlsx
📊 工作表: Sheet1
📍 位置: B2 (第2行, 第2列)
📝 內容: product liability

──────────────────────────────────────────────────────────────────────
結果 2
📄 檔案: Start of the art evaluation_Hibiscus2.xlsx
📊 工作表: Sheet1
📍 位置: C4 (第4行, 第3列)
📝 內容: Product stability
📋 完整行資料:
   B4     = audio code
   C4     = Product stability ← 匹配
   D4     = Medium
   E4     = mechnial design for optimation
```

**搜索特點：**
- ✅ 不區分大小寫
- ✅ 部分匹配（包含關鍵詞即可）
- ✅ 高亮關鍵詞（黃色顯示）
- ✅ 顯示檔案位置

---

### 3. stats - 查看統計

```bash
python3 excel_search_cli.py stats
```

**輸出範例：**
```
======================================================================
  📊 資料庫統計
======================================================================

📁 索引檔案數:     6
📝 總單元格數:     2,588
💾 檔案總大小:     2.13 MB
🗄️  資料庫大小:     1.0 MB
📊 平均單元格/檔案: 431
🕒 最後索引時間:   2026-01-06 18:00:18

📋 最近索引的檔案:
  1. Template Driver_Verification_List.xlsx (774 單元格)
  2. 8D Report & Problem Solving Sheet.xlsx (773 單元格)
  ...
```

---

### 4. info - 系統資訊

```bash
python3 excel_search_cli.py info
```

顯示資料庫路徑、大小、Python 版本等資訊。

---

### 5. clear - 清空資料庫

```bash
python3 excel_search_cli.py clear
```

**注意：** 會要求確認！

---

## 💡 使用場景

### 場景 1：首次使用

```bash
# 1. 索引所有 Excel 檔案
python3 excel_search_cli.py index Sharepoint

# 2. 查看統計
python3 excel_search_cli.py stats

# 3. 開始搜索
python3 excel_search_cli.py search "你的關鍵詞"
```

---

### 場景 2：新增檔案後更新

```bash
# 重新索引（會自動處理新增/修改的檔案）
python3 excel_search_cli.py index Sharepoint
```

---

### 場景 3：查找測試用例

```bash
# 搜索測試相關的內容
python3 excel_search_cli.py search "test" --limit 20

# 顯示完整行，查看更多上下文
python3 excel_search_cli.py search "test" --full-row
```

---

### 場景 4：查找產品型號

```bash
# 搜索產品編號
python3 excel_search_cli.py search "PN3004"

# 搜索 USB 相關
python3 excel_search_cli.py search "USB" --full-row
```

---

## 🔧 進階技巧

### 1. 使用管道（Pipe）

```bash
# 搜索後導出到文字檔
python3 excel_search_cli.py search "USB" > usb_results.txt
```

### 2. 批次索引特定目錄

```bash
# 只索引特定子目錄
python3 excel_search_cli.py index "Sharepoint/Deneb - Documents" --recursive
```

### 3. 查看資料庫大小

```bash
# 查看資料庫檔案
ls -lh excel_search.db

# 或使用 info 命令
python3 excel_search_cli.py info
```

---

## ⚠️ 注意事項

### 1. 支援的檔案格式

目前簡化版只支援：
- ✅ `.xlsx` (Excel 2007+)
- ❌ `.xls` (舊版，需要擴展支援)

### 2. 效能建議

- **小型資料集（< 100 檔案）**：隨時重新索引
- **大型資料集（> 500 檔案）**：建議定期更新索引

### 3. 資料庫位置

預設資料庫：`excel_search.db`（在當前目錄）

可在 `config.py` 中修改路徑。

---

## 🐛 常見問題

### Q: 搜索沒有結果？

**檢查：**
1. 是否已經索引該檔案？ → 執行 `stats` 查看
2. 關鍵詞拼寫是否正確？
3. 關鍵詞是否太短？（建議至少 3 個字符）

### Q: 索引失敗？

**可能原因：**
1. 檔案損壞
2. 密碼保護
3. 不支援的格式（.xls）

**解決：** 查看錯誤訊息，跳過問題檔案

### Q: 如何重建索引？

```bash
# 清空舊資料庫
python3 excel_search_cli.py clear

# 重新索引
python3 excel_search_cli.py index Sharepoint
```

---

## 📊 效能參考

實測資料（你的環境）：

| 檔案數 | 單元格數 | 索引時間 | 資料庫大小 | 搜索時間 |
|--------|---------|---------|-----------|---------|
| 6      | 2,588   | < 1 秒  | 1.0 MB    | < 0.1 秒 |
| 332    | ~100萬  | 預估 5-10 分鐘 | 預估 500 MB | < 2 秒 |

---

## 🎯 下一步擴展

目前的簡化版已經可以使用，未來可以擴展：

1. ✅ 支援 `.xls` 格式（使用 xlrd）
2. ✅ 處理合併儲存格
3. ✅ 多線程索引（加速）
4. ✅ 增量更新（只索引新增/修改的檔案）
5. ✅ Web 介面
6. ✅ 導出搜索結果為 CSV

---

## 📞 需要幫助？

查看開發流程文件：`開發流程/開發進度規劃.txt`

---

**版本：** 1.0.0
**更新日期：** 2026-01-06
