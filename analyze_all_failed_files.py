#!/usr/bin/env python3
"""
完整分析所有失敗的檔案（快速版本）
只檢查檔案格式和基本資訊，不實際打開檔案
"""
import os
import zipfile
from file_scanner import FileScanner
from database_mariadb import DatabaseManager

def quick_check_file(file_path):
    """快速檢查檔案類型（不打開）"""
    # 1. 檢查副檔名
    if file_path.endswith('.xls') and not file_path.endswith('.xlsx'):
        return 'xls_format', '.xls 舊格式'

    # 2. 檢查檔案大小
    try:
        size = os.path.getsize(file_path)
        if size == 0:
            return 'empty', '空檔案'
    except:
        return 'access_error', '無法存取'

    # 3. 檢查 ZIP 格式（快速）
    try:
        with zipfile.ZipFile(file_path, 'r') as zf:
            # 嘗試讀取檔案列表
            files = zf.namelist()
            # Excel 檔案應該有這些基本檔案
            if '[Content_Types].xml' in files or 'xl/workbook.xml' in files:
                return 'valid_xlsx', '有效的 .xlsx（但索引時失敗）'
            else:
                return 'invalid_structure', 'ZIP 格式但非 Excel 結構'
    except zipfile.BadZipFile:
        return 'corrupted_zip', 'ZIP 結構損壞'
    except Exception as e:
        return 'unknown_error', f'未知錯誤: {str(e)[:50]}'

def main():
    print("=" * 70)
    print("  🔍 完整分析所有失敗檔案")
    print("=" * 70)
    print()

    # 1. 掃描所有檔案
    print("📂 掃描 Sharepoint 目錄...")
    scanner = FileScanner()
    all_files = scanner.scan_directory('./Sharepoint', recursive=True, show_progress=False)
    print(f"✅ 找到 {len(all_files)} 個 Excel 檔案")
    print()

    # 2. 獲取已成功索引的檔案
    print("📊 檢查資料庫中已索引的檔案...")
    with DatabaseManager() as db:
        if not db.connection:
            print("❌ 無法連接資料庫")
            return
        db.cursor.execute("SELECT file_path FROM files")
        indexed_files = {row['file_path'] for row in db.cursor.fetchall()}

    print(f"✅ 已索引 {len(indexed_files)} 個檔案")
    print()

    # 3. 找出未索引的檔案
    failed_files = []
    for file_info in all_files:
        if file_info['file_path'] not in indexed_files:
            failed_files.append(file_info)

    print(f"❌ 失敗 {len(failed_files)} 個檔案")
    print()

    # 4. 快速分析所有失敗檔案
    print("🔍 分析所有失敗檔案...")
    print()

    failure_stats = {}
    detailed_results = []

    for i, file_info in enumerate(failed_files, 1):
        file_path = file_info['file_path']
        file_name = file_info['file_name']

        # 快速檢查
        error_type, error_msg = quick_check_file(file_path)

        # 統計
        if error_type not in failure_stats:
            failure_stats[error_type] = []
        failure_stats[error_type].append(file_name)

        # 記錄詳細結果
        detailed_results.append({
            'name': file_name,
            'path': file_path,
            'type': error_type,
            'message': error_msg
        })

        # 進度顯示
        if i % 10 == 0:
            print(f"  進度: {i}/{len(failed_files)}")

    print(f"✅ 分析完成！")
    print()

    # 5. 顯示統計結果
    print("=" * 70)
    print("  📊 失敗原因統計")
    print("=" * 70)
    print()

    # 定義錯誤類型的中文說明
    error_descriptions = {
        'xls_format': '🔴 .xls 舊格式（openpyxl 不支援）',
        'corrupted_zip': '🔴 ZIP 結構損壞',
        'invalid_structure': '🟡 ZIP 正常但非 Excel 結構',
        'valid_xlsx': '🟢 有效 .xlsx（其他原因失敗）',
        'empty': '⚪ 空檔案',
        'access_error': '🔵 無法存取',
        'unknown_error': '⚫ 未知錯誤'
    }

    # 按數量排序
    sorted_stats = sorted(failure_stats.items(), key=lambda x: len(x[1]), reverse=True)

    for error_type, files in sorted_stats:
        desc = error_descriptions.get(error_type, error_type)
        count = len(files)
        percentage = (count / len(failed_files)) * 100
        print(f"{desc}")
        print(f"  數量: {count} 個 ({percentage:.1f}%)")
        print()

    # 6. 保存詳細報告
    report_file = '失敗檔案完整分析報告.txt'
    with open(report_file, 'w', encoding='utf-8') as f:
        f.write("=" * 70 + "\n")
        f.write("  失敗檔案完整分析報告\n")
        f.write("=" * 70 + "\n\n")

        f.write(f"總失敗檔案: {len(failed_files)} 個\n\n")

        # 按類型分組
        f.write("=" * 70 + "\n")
        f.write("  按失敗類型分組\n")
        f.write("=" * 70 + "\n\n")

        for error_type, files in sorted_stats:
            desc = error_descriptions.get(error_type, error_type)
            f.write(f"\n{desc} ({len(files)} 個)\n")
            f.write("-" * 70 + "\n")
            for fname in files:
                f.write(f"  • {fname}\n")

        # 詳細清單
        f.write("\n\n")
        f.write("=" * 70 + "\n")
        f.write("  詳細清單（按檔名排序）\n")
        f.write("=" * 70 + "\n\n")

        for result in sorted(detailed_results, key=lambda x: x['name']):
            f.write(f"檔案: {result['name']}\n")
            f.write(f"  路徑: {result['path']}\n")
            f.write(f"  類型: {result['type']}\n")
            f.write(f"  說明: {result['message']}\n")
            f.write("\n")

    print(f"📄 詳細報告已保存: {report_file}")
    print()

    # 7. 建議
    print("=" * 70)
    print("  💡 處理建議")
    print("=" * 70)
    print()

    if 'xls_format' in failure_stats:
        xls_count = len(failure_stats['xls_format'])
        print(f"1️⃣  .xls 舊格式 ({xls_count} 個)")
        print("   • 安裝 xlrd 模組")
        print("   • 修改程式碼支援 .xls 讀取")
        print(f"   • 可增加索引: 約 {xls_count} 個檔案")
        print()

    if 'corrupted_zip' in failure_stats:
        corrupted_count = len(failure_stats['corrupted_zip'])
        print(f"2️⃣  ZIP 損壞 ({corrupted_count} 個)")
        print("   • 從 Sharepoint 重新下載")
        print("   • 用 Excel 打開並修復")
        print("   • 或用 zip -FF 工具嘗試修復")
        print()

    if 'valid_xlsx' in failure_stats:
        valid_count = len(failure_stats['valid_xlsx'])
        print(f"3️⃣  有效但失敗 ({valid_count} 個)")
        print("   • 這些檔案 ZIP 結構正常")
        print("   • 可能是內部結構問題")
        print("   • 建議手動測試開啟")
        print()

    # 8. 可修復檔案統計
    repairable = 0
    if 'xls_format' in failure_stats:
        repairable += len(failure_stats['xls_format'])
    if 'valid_xlsx' in failure_stats:
        repairable += len(failure_stats['valid_xlsx'])

    print("=" * 70)
    print("  📈 可修復性評估")
    print("=" * 70)
    print()
    print(f"✅ 可修復: {repairable} 個 ({(repairable/len(failed_files)*100):.1f}%)")
    print(f"⚠️  需努力: {len(failed_files) - repairable} 個")
    print()

if __name__ == '__main__':
    main()
