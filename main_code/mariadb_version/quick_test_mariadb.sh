#!/bin/bash

echo "=========================================="
echo "  Excel 搜索系統 - MariaDB 完整測試指南"
echo "=========================================="
echo ""

# ============================================================================
# 一、基本功能測試
# ============================================================================

echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo "  📋 一、基本功能測試"
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo ""

# 測試 1：系統資訊
echo "ℹ️  測試 1：查看系統資訊"
echo "------------------------------------------"
python3 excel_search_cli_mariadb.py info
echo ""

# 測試 2：資料庫統計
echo "📊 測試 2：查看資料庫統計"
echo "------------------------------------------"
python3 excel_search_cli_mariadb.py stats
echo ""

# ============================================================================
# 二、索引功能測試
# ============================================================================

echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo "  📥 二、索引功能測試"
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo ""

# 測試 3：增量索引（預設，推薦）
echo "🔄 測試 3：增量索引（智慧同步）"
echo "------------------------------------------"
echo "說明：只處理新增/修改的檔案，跳過未變動檔案"
echo "指令："
echo "  python3 excel_search_cli_mariadb.py index \"Sharepoint\""
echo ""
echo "按 Enter 繼續測試，或 Ctrl+C 跳過..."
read -r
python3 excel_search_cli_mariadb.py index "Sharepoint"
echo ""

# 測試 4：指定增量模式
echo "🔄 測試 4：明確指定增量模式"
echo "------------------------------------------"
echo "指令："
echo "  python3 excel_search_cli_mariadb.py index \"Sharepoint\" --incremental"
echo ""

# 測試 5：全量重新索引
echo "♻️  測試 5：全量重新索引"
echo "------------------------------------------"
echo "說明：清空並重新索引所有檔案（慎用）"
echo "指令："
echo "  python3 excel_search_cli_mariadb.py index \"Sharepoint\" --full"
echo ""

# 測試 6：不遞迴索引（只索引當前目錄）
echo "📁 測試 6：只索引單一目錄（不包含子目錄）"
echo "------------------------------------------"
echo "指令："
echo "  python3 excel_search_cli_mariadb.py index \"Sharepoint/某個目錄\" --no-recursive"
echo ""

# ============================================================================
# 三、搜索功能測試
# ============================================================================

echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo "  🔍 三、搜索功能測試"
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo ""

# 測試 7：基本搜索
echo "🔍 測試 7：基本搜索（預設 20 筆）"
echo "------------------------------------------"
python3 excel_search_cli_mariadb.py search "test"
echo ""

# 測試 8：限制結果數量
echo "🔍 測試 8：限制搜索結果（5 筆）"
echo "------------------------------------------"
python3 excel_search_cli_mariadb.py search "Hibiscus" --limit 5
echo ""

# 測試 9：顯示完整內容
echo "🔍 測試 9：顯示完整單元格內容（不截斷）"
echo "------------------------------------------"
python3 excel_search_cli_mariadb.py search "Driver" --full-row --limit 3
echo ""

# 測試 10：中文搜索
echo "🔍 測試 10：中文關鍵詞搜索"
echo "------------------------------------------"
python3 excel_search_cli_mariadb.py search "鏡頭" --limit 5
echo ""

# 測試 11：數字搜索
echo "🔍 測試 11：數字搜索"
echo "------------------------------------------"
python3 excel_search_cli_mariadb.py search "12345" --limit 5
echo ""

# ============================================================================
# 四、增量索引場景測試
# ============================================================================

echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo "  🧪 四、增量索引場景測試"
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo ""

echo "📖 增量索引會自動處理以下三種檔案變動："
echo ""
echo "  ➕ 場景 1：新增檔案"
echo "     當有新的 Excel 檔案加入目錄時"
echo "     → 自動偵測並索引新檔案"
echo ""
echo "  🔄 場景 2：修改檔案"
echo "     當現有 Excel 檔案內容被修改時"
echo "     → 刪除舊資料，重新索引"
echo ""
echo "  🗑️  場景 3：刪除檔案"
echo "     當 Excel 檔案從目錄移除時"
echo "     → 自動清理資料庫中的孤兒資料"
echo ""
echo "  ⏭️  場景 4：未變動檔案"
echo "     檔案修改時間未改變"
echo "     → 跳過處理，節省時間"
echo ""

# ============================================================================
# 五、實際場景操作演示
# ============================================================================

echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo "  🎯 五、實際場景操作演示"
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo ""

echo "以下是實際使用的完整流程示範："
echo ""

# 場景 A：新增檔案
echo "➕ 場景 A：新增檔案測試"
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo "步驟："
echo "  1. 複製一個測試檔案到 Sharepoint 目錄"
echo "     cp 測試檔案.xlsx Sharepoint/測試檔案.xlsx"
echo ""
echo "  2. 執行增量索引"
echo "     python3 excel_search_cli_mariadb.py index \"Sharepoint\""
echo ""
echo "  3. 檢查統計（應該看到檔案數量 +1）"
echo "     python3 excel_search_cli_mariadb.py stats"
echo ""
echo "  4. 搜索新檔案內容"
echo "     python3 excel_search_cli_mariadb.py search \"<檔案中的關鍵字>\""
echo ""

# 場景 B：修改檔案
echo "🔄 場景 B：修改檔案測試"
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo "步驟："
echo "  1. 用 Excel 或 LibreOffice 修改檔案內容"
echo "     libreoffice Sharepoint/測試檔案.xlsx"
echo "     （修改某個單元格，然後儲存）"
echo ""
echo "  2. 執行增量索引"
echo "     python3 excel_search_cli_mariadb.py index \"Sharepoint\""
echo ""
echo "  3. 應該看到輸出："
echo "     🔄 更新檔案: 1"
echo "     （表示偵測到修改並重新索引）"
echo ""
echo "  4. 搜索修改後的內容"
echo "     python3 excel_search_cli_mariadb.py search \"<新增的關鍵字>\""
echo ""

# 場景 C：刪除檔案
echo "🗑️  場景 C：刪除檔案測試"
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo "步驟："
echo "  1. 刪除測試檔案"
echo "     rm Sharepoint/測試檔案.xlsx"
echo ""
echo "  2. 執行增量索引"
echo "     python3 excel_search_cli_mariadb.py index \"Sharepoint\""
echo ""
echo "  3. 應該看到輸出："
echo "     🔍 檢查已刪除的檔案..."
echo "     🗑️  清除: 測試檔案.xlsx (已刪除)"
echo "     🗑️  清除檔案: 1"
echo ""
echo "  4. 檢查統計（檔案數量應該減少）"
echo "     python3 excel_search_cli_mariadb.py stats"
echo ""
echo "  5. 搜索原本的內容（應該找不到）"
echo "     python3 excel_search_cli_mariadb.py search \"<原本的關鍵字>\""
echo ""

# 場景 D：未變動檔案
echo "⏭️  場景 D：未變動檔案（效能測試）"
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo "步驟："
echo "  1. 不做任何修改，直接執行增量索引"
echo "     python3 excel_search_cli_mariadb.py index \"Sharepoint\""
echo ""
echo "  2. 應該看到："
echo "     ⏭️  跳過檔案: <大部分檔案>"
echo "     （處理速度非常快，只需 0.2-0.5 秒）"
echo ""
echo "  3. 比較全量索引的時間差異"
echo "     time python3 excel_search_cli_mariadb.py index \"Sharepoint\" --full"
echo "     （全量索引可能需要 200+ 秒）"
echo ""

# ============================================================================
# 六、進階指令參考
# ============================================================================

echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo "  📚 六、進階指令參考"
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo ""

cat << 'EOF'
# 1. 索引指令
# ============================================================================

# 增量索引（預設，推薦）
python3 excel_search_cli_mariadb.py index "Sharepoint"
python3 excel_search_cli_mariadb.py index "Sharepoint" --incremental

# 全量重新索引
python3 excel_search_cli_mariadb.py index "Sharepoint" --full

# 不遞迴（只索引當前目錄）
python3 excel_search_cli_mariadb.py index "Sharepoint/某目錄" --no-recursive

# 索引特定子目錄
python3 excel_search_cli_mariadb.py index "Sharepoint/Hibiscus2 - Documents"

# 結合選項
python3 excel_search_cli_mariadb.py index "路徑" --no-recursive --full


# 2. 搜索指令
# ============================================================================

# 基本搜索（預設 20 筆結果）
python3 excel_search_cli_mariadb.py search "關鍵詞"

# 限制結果數量
python3 excel_search_cli_mariadb.py search "關鍵詞" --limit 5
python3 excel_search_cli_mariadb.py search "關鍵詞" --limit 100

# 顯示完整內容（不截斷）
python3 excel_search_cli_mariadb.py search "關鍵詞" --full-row

# 結合選項
python3 excel_search_cli_mariadb.py search "關鍵詞" --limit 10 --full-row

# 搜索中文
python3 excel_search_cli_mariadb.py search "鏡頭"

# 搜索數字
python3 excel_search_cli_mariadb.py search "12345"

# 搜索特殊字元（需要引號）
python3 excel_search_cli_mariadb.py search "IR-LED-001"


# 3. 統計與資訊
# ============================================================================

# 查看資料庫統計
python3 excel_search_cli_mariadb.py stats

# 查看系統資訊
python3 excel_search_cli_mariadb.py info


# 4. 資料庫管理
# ============================================================================

# 清空資料庫（會要求確認）
python3 excel_search_cli_mariadb.py clear

# 直接確認清空（自動化腳本用）
yes | python3 excel_search_cli_mariadb.py clear


# 5. 效能比較
# ============================================================================

# 測量增量索引時間
time python3 excel_search_cli_mariadb.py index "Sharepoint"

# 測量全量索引時間
time python3 excel_search_cli_mariadb.py index "Sharepoint" --full

# 測量搜索時間
time python3 excel_search_cli_mariadb.py search "test" --limit 100


# 6. 管道與自動化
# ============================================================================

# 儲存搜索結果到檔案
python3 excel_search_cli_mariadb.py search "test" > 搜索結果.txt

# 儲存統計資訊
python3 excel_search_cli_mariadb.py stats > 資料庫統計.txt

# 批次搜索多個關鍵字
for keyword in "test" "driver" "LED"; do
    echo "搜索: $keyword"
    python3 excel_search_cli_mariadb.py search "$keyword" --limit 5
    echo ""
done


# 7. 實用組合指令
# ============================================================================

# 索引後立即查看統計
python3 excel_search_cli_mariadb.py index "Sharepoint" && \
python3 excel_search_cli_mariadb.py stats

# 清空後重新索引
python3 excel_search_cli_mariadb.py clear && \
python3 excel_search_cli_mariadb.py index "Sharepoint" --full

# 多目錄索引
python3 excel_search_cli_mariadb.py index "Sharepoint/Hibiscus2 - Documents" && \
python3 excel_search_cli_mariadb.py index "Sharepoint/Deneb - Documents" && \
python3 excel_search_cli_mariadb.py stats


# 8. 監控與除錯
# ============================================================================

# 詳細輸出（使用 -v 如果支援）
python3 excel_search_cli_mariadb.py index "Sharepoint" 2>&1 | tee 索引日誌.txt

# 只顯示錯誤
python3 excel_search_cli_mariadb.py index "Sharepoint" 2>&1 | grep "❌"

# 監控資料庫大小變化
watch -n 5 'python3 excel_search_cli_mariadb.py stats | grep "資料庫大小"'

EOF

echo ""

# ============================================================================
# 七、索引判斷邏輯說明
# ============================================================================

echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo "  🧠 七、增量索引判斷邏輯"
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo ""

cat << 'EOF'
增量索引使用以下邏輯判斷檔案狀態：

┌─────────────────────────────────────────────────────────────┐
│  檔案狀態判斷流程                                           │
└─────────────────────────────────────────────────────────────┘

1️⃣  掃描檔案系統
   └─ 找到所有 .xlsx 和 .xlsm 檔案
   └─ 記錄每個檔案的 last_modified 時間戳

2️⃣  查詢資料庫
   └─ 檢查檔案路徑是否存在於 files 表
   └─ 若存在，取得資料庫中的 last_modified

3️⃣  比對時間戳（增量模式）
   ├─ 檔案不存在於資料庫
   │  └─ ➕ 判定：新增檔案
   │  └─ 動作：直接索引
   │
   ├─ 檔案存在，且時間戳相同或更舊
   │  └─ ⏭️  判定：未變動
   │  └─ 動作：跳過處理
   │
   └─ 檔案存在，但時間戳變新
      └─ 🔄 判定：已修改
      └─ 動作：刪除舊資料 → 重新索引

4️⃣  反向比對（檢查刪除）
   └─ 取得資料庫中該路徑下所有檔案
   └─ 檢查每個檔案是否還存在於檔案系統
   └─ 若不存在
      └─ 🗑️  判定：已刪除
      └─ 動作：從資料庫移除（CASCADE 自動刪除相關單元格）

┌─────────────────────────────────────────────────────────────┐
│  效能數據（基於 332 個檔案）                                │
└─────────────────────────────────────────────────────────────┘

全量索引：  238 秒    （每次都處理所有檔案）
增量索引：  0.236 秒  （只處理變動檔案）

提升倍數：  1,008 倍  ⚡

┌─────────────────────────────────────────────────────────────┐
│  技術細節                                                   │
└─────────────────────────────────────────────────────────────┘

✓ 比對層級：檔案級別（非儲存格級別）
✓ 時間來源：檔案系統的 os.path.getmtime()
✓ 儲存格處理：利用 ON DELETE CASCADE 自動處理
✓ 查詢效能：使用主鍵和索引，查詢極快

EOF

echo ""

# ============================================================================
# 八、常見問題 FAQ
# ============================================================================

echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo "  ❓ 八、常見問題 FAQ"
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo ""

cat << 'EOF'
Q1: 我有新增檔案，要用什麼指令？
A1: 直接執行增量索引即可：
    python3 excel_search_cli_mariadb.py index "Sharepoint"
    系統會自動偵測新檔案並索引。

Q2: 我修改了檔案內容，要重新索引嗎？
A2: 是的，執行增量索引：
    python3 excel_search_cli_mariadb.py index "Sharepoint"
    系統會偵測到修改時間變更，自動刪除舊資料並重新索引。

Q3: 我刪除了一些檔案，資料庫會自動清理嗎？
A3: 會的！增量索引包含反向比對功能，會自動清理已刪除檔案。

Q4: 增量索引和全量索引差在哪？
A4: 增量索引只處理變動檔案（新增/修改/刪除），全量索引會重新處理所有檔案。
    增量索引快 1000+ 倍，建議日常使用。

Q5: 什麼時候需要用全量索引？
A5: 只有在以下情況：
    - 懷疑資料庫損壞
    - 需要完全重建索引
    - 資料庫結構變更後
    日常使用一律建議增量索引。

Q6: 搜索結果太多，怎麼限制數量？
A6: 使用 --limit 參數：
    python3 excel_search_cli_mariadb.py search "關鍵詞" --limit 10

Q7: 搜索結果被截斷，怎麼看完整內容？
A7: 使用 --full-row 參數：
    python3 excel_search_cli_mariadb.py search "關鍵詞" --full-row

Q8: ZIP 損壞的檔案會一直重試索引嗎？
A8: 目前會的。這是已知的改進點，未來會新增失敗檔案記錄機制。

Q9: .xls 舊格式檔案不能索引嗎？
A9: 目前不支援。可以手動轉換成 .xlsx，或等待未來版本支援 xlrd。

Q10: 如何檢查索引是否成功？
A10: 執行統計指令：
     python3 excel_search_cli_mariadb.py stats
     會顯示檔案總數、單元格總數等資訊。

EOF

echo ""

# ============================================================================
# 結尾
# ============================================================================

echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo "  ✅ 測試指南結束"
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo ""
echo "💡 提示："
echo "  • 日常使用推薦：增量索引（預設）"
echo "  • 首次建立索引：使用全量索引或增量索引皆可"
echo "  • 定期執行：建議每天或每週執行一次增量索引"
echo "  • 效能最佳：增量索引速度快 1000+ 倍"
echo ""
echo "📖 詳細文件："
echo "  • MariaDB版本使用說明.md"
echo "  • 每日進度/工作日誌_2026-01-08.md"
echo ""
echo "🔗 快速開始："
echo "  python3 excel_search_cli_mariadb.py index \"Sharepoint\""
echo "  python3 excel_search_cli_mariadb.py search \"你的關鍵字\""
echo ""
