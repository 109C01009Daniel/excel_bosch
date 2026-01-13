#!/usr/bin/env python3
"""
分析索引失敗的檔案
"""
import os
from pathlib import Path
from openpyxl import load_workbook
from file_scanner import FileScanner
from database_mariadb import DatabaseManager

def main():
    print("=" * 70)
    print("  🔍 分析索引失敗的檔案")
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

    # 4. 分析失敗原因
    print("=" * 70)
    print("  📋 失敗原因分析")
    print("=" * 70)
    print()

    failure_reasons = {
        'xls_format': [],      # .xls 舊格式
        'not_zip': [],         # 不是 zip 格式
        'password': [],        # 密碼保護
        'corrupted': [],       # 檔案損壞
        'other': []            # 其他錯誤
    }

    for file_info in failed_files[:20]:  # 只檢查前20個，避免太慢
        file_path = file_info['file_path']
        file_name = file_info['file_name']

        # 檢查是否是 .xls 格式
        if file_path.endswith('.xls') and not file_path.endswith('.xlsx'):
            failure_reasons['xls_format'].append(file_name)
            continue

        # 嘗試打開檔案
        try:
            wb = load_workbook(file_path, read_only=True, data_only=True)
            wb.close()
            failure_reasons['other'].append(file_name)
        except Exception as e:
            error_msg = str(e).lower()
            if 'not a zip file' in error_msg or 'not zip' in error_msg:
                failure_reasons['not_zip'].append(file_name)
            elif 'password' in error_msg or 'encrypted' in error_msg:
                failure_reasons['password'].append(file_name)
            elif 'corrupt' in error_msg or 'damaged' in error_msg:
                failure_reasons['corrupted'].append(file_name)
            else:
                failure_reasons['other'].append(file_name)

    # 5. 顯示統計
    print(f"🔴 .xls 舊格式:        {len(failure_reasons['xls_format'])} 個")
    print(f"🔴 檔案格式錯誤:      {len(failure_reasons['not_zip'])} 個")
    print(f"🔴 密碼保護:          {len(failure_reasons['password'])} 個")
    print(f"🔴 檔案損壞:          {len(failure_reasons['corrupted'])} 個")
    print(f"🔴 其他原因:          {len(failure_reasons['other'])} 個")
    print()

    # 6. 顯示範例
    if failure_reasons['xls_format']:
        print("📌 .xls 舊格式範例 (前5個):")
        for fname in failure_reasons['xls_format'][:5]:
            print(f"   • {fname}")
        print()

    if failure_reasons['not_zip']:
        print("📌 格式錯誤範例 (前5個):")
        for fname in failure_reasons['not_zip'][:5]:
            print(f"   • {fname}")
        print()

    if failure_reasons['password']:
        print("📌 密碼保護範例 (前5個):")
        for fname in failure_reasons['password'][:5]:
            print(f"   • {fname}")
        print()

    # 7. 建議
    print("=" * 70)
    print("  💡 解決建議")
    print("=" * 70)
    print()

    if failure_reasons['xls_format']:
        print("1️⃣  .xls 舊格式檔案:")
        print("   • 使用 xlrd 庫讀取")
        print("   • 或手動轉換成 .xlsx 格式")
        print()

    if failure_reasons['not_zip']:
        print("2️⃣  格式錯誤的檔案:")
        print("   • 可能是檔案損壞")
        print("   • 嘗試用 Excel 打開並另存為新檔")
        print()

    if failure_reasons['password']:
        print("3️⃣  密碼保護的檔案:")
        print("   • 需要先解除密碼保護")
        print("   • 或提供密碼給索引程式")
        print()

if __name__ == '__main__':
    main()
