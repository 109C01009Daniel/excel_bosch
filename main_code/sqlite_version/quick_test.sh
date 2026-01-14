#!/bin/bash

echo "=========================================="
echo "  Excel 搜索系統 - 快速測試指南"
echo "=========================================="
echo ""

# 測試 1：查看統計
echo "📊 測試 1：查看資料庫統計"
echo "------------------------------------------"
python3 excel_search_cli.py stats
echo ""

# 測試 2：搜索 "test"
echo "🔍 測試 2：搜索 'test' 關鍵詞"
echo "------------------------------------------"
python3 excel_search_cli.py search "test" --limit 5
echo ""

# 測試 3：搜索 "Hibiscus"
echo "🔍 測試 3：搜索 'Hibiscus' 關鍵詞"
echo "------------------------------------------"
python3 excel_search_cli.py search "Hibiscus" --limit 5
echo ""

# 測試 4：搜索 "Driver" 並顯示完整行
echo "🔍 測試 4：搜索 'Driver' 並顯示完整行"
echo "------------------------------------------"
python3 excel_search_cli.py search "Driver" --full-row --limit 3
echo ""

echo "✅ 快速測試完成！"
