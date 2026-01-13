#!/usr/bin/env python3
"""
生成完整的檔案狀態清單
包含所有 Excel 檔案的詳細資訊和狀態
"""
import os
import zipfile
from file_scanner import FileScanner
from database_mariadb import DatabaseManager

def check_file_status(file_path):
    """
    詳細檢查檔案狀態
    返回: (狀態代碼, 詳細說明, 檔案大小)
    """
    try:
        file_size = os.path.getsize(file_path)
    except:
        return 'ERROR_ACCESS', '無法存取檔案', 0

    # 空檔案
    if file_size == 0:
        return 'ERROR_EMPTY', '空檔案 (0 bytes)', file_size

    # 檢查副檔名
    if file_path.endswith('.xls') and not file_path.endswith('.xlsx'):
        return 'ERROR_XLS', '.xls 舊格式 (openpyxl 不支援)', file_size

    # 檢查 ZIP 格式
    try:
        # 先讀取檔頭
        with open(file_path, 'rb') as f:
            header = f.read(4)
            if header[:2] != b'PK':
                return 'ERROR_NOT_ZIP', '不是 ZIP 格式 (檔頭錯誤)', file_size

        # 嘗試打開 ZIP
        with zipfile.ZipFile(file_path, 'r') as zf:
            files = zf.namelist()

            # 檢查是否有 Excel 的基本結構
            has_content_types = '[Content_Types].xml' in files
            has_workbook = any('workbook.xml' in f for f in files)

            if not has_content_types and not has_workbook:
                return 'ERROR_STRUCTURE', 'ZIP 正常但缺少 Excel 結構', file_size

            # ZIP 和結構都正常
            return 'VALID_ZIP', 'ZIP 結構完整 (應該可以索引)', file_size

    except zipfile.BadZipFile:
        return 'ERROR_CORRUPT', 'ZIP 結構損壞 (無法解壓)', file_size
    except Exception as e:
        return 'ERROR_UNKNOWN', f'未知錯誤: {str(e)[:50]}', file_size

def format_size(size_bytes):
    """格式化檔案大小"""
    for unit in ['B', 'KB', 'MB', 'GB']:
        if size_bytes < 1024.0:
            return f"{size_bytes:.2f} {unit}"
        size_bytes /= 1024.0
    return f"{size_bytes:.2f} TB"

def main():
    print("=" * 70)
    print("  📋 生成完整檔案狀態清單")
    print("=" * 70)
    print()

    # 1. 掃描所有檔案
    print("📂 掃描 Sharepoint 目錄...")
    scanner = FileScanner()
    all_files = scanner.scan_directory('./Sharepoint', recursive=True, show_progress=False)
    print(f"✅ 找到 {len(all_files)} 個 Excel 檔案")
    print()

    # 2. 獲取已成功索引的檔案
    print("📊 檢查資料庫...")
    with DatabaseManager() as db:
        if not db.connection:
            print("❌ 無法連接資料庫")
            return

        db.cursor.execute("SELECT file_path, cell_count, indexed_at FROM files")
        indexed_data = {}
        for row in db.cursor.fetchall():
            indexed_data[row['file_path']] = {
                'cell_count': row['cell_count'],
                'indexed_at': str(row['indexed_at'])
            }

    print(f"✅ 已索引 {len(indexed_data)} 個檔案")
    print()

    # 3. 分析每個檔案
    print("🔍 分析所有檔案...")
    results = []

    for i, file_info in enumerate(all_files, 1):
        file_path = file_info['file_path']
        file_name = file_info['file_name']

        # 檢查是否已索引
        if file_path in indexed_data:
            status = 'SUCCESS'
            detail = f"✅ 已索引 ({indexed_data[file_path]['cell_count']} 個單元格)"
            size = file_info['file_size']
        else:
            # 檢查失敗原因
            status, detail, size = check_file_status(file_path)

        results.append({
            'name': file_name,
            'path': file_path,
            'status': status,
            'detail': detail,
            'size': size
        })

        # 進度顯示
        if i % 20 == 0:
            print(f"  進度: {i}/{len(all_files)}")

    print(f"✅ 分析完成！")
    print()

    # 4. 統計
    stats = {}
    for result in results:
        status = result['status']
        if status not in stats:
            stats[status] = 0
        stats[status] += 1

    print("=" * 70)
    print("  📊 統計資訊")
    print("=" * 70)
    print()

    status_names = {
        'SUCCESS': '✅ 成功索引',
        'ERROR_XLS': '🔴 .xls 舊格式',
        'ERROR_CORRUPT': '🔴 ZIP 損壞',
        'ERROR_STRUCTURE': '🟡 結構異常',
        'VALID_ZIP': '🟢 ZIP 正常（但失敗）',
        'ERROR_EMPTY': '⚪ 空檔案',
        'ERROR_ACCESS': '🔵 無法存取',
        'ERROR_NOT_ZIP': '🟠 非 ZIP 格式',
        'ERROR_UNKNOWN': '⚫ 未知錯誤'
    }

    for status, count in sorted(stats.items(), key=lambda x: x[1], reverse=True):
        name = status_names.get(status, status)
        percentage = (count / len(results)) * 100
        print(f"{name}: {count} 個 ({percentage:.1f}%)")
    print()

    # 5. 生成詳細報告（CSV 格式，方便 Excel 打開）
    csv_file = '完整檔案狀態清單.csv'
    print(f"📄 生成 CSV 報告: {csv_file}")

    with open(csv_file, 'w', encoding='utf-8-sig') as f:  # utf-8-sig 讓 Excel 正確顯示中文
        # CSV 標題
        f.write("狀態,檔案名稱,完整路徑,檔案大小,詳細說明\n")

        # 按狀態排序
        for result in sorted(results, key=lambda x: (x['status'], x['name'])):
            status_icon = status_names.get(result['status'], result['status'])
            f.write(f'"{status_icon}",')
            f.write(f'"{result["name"]}",')
            f.write(f'"{result["path"]}",')
            f.write(f'"{format_size(result["size"])}",')
            f.write(f'"{result["detail"]}"\n')

    print(f"✅ CSV 報告已生成")
    print()

    # 6. 生成文字報告（詳細版）
    txt_file = '完整檔案狀態清單.txt'
    print(f"📄 生成文字報告: {txt_file}")

    with open(txt_file, 'w', encoding='utf-8') as f:
        f.write("=" * 70 + "\n")
        f.write("  完整檔案狀態清單\n")
        f.write("=" * 70 + "\n\n")

        f.write(f"總檔案數: {len(results)} 個\n\n")

        # 統計
        f.write("統計資訊:\n")
        f.write("-" * 70 + "\n")
        for status, count in sorted(stats.items(), key=lambda x: x[1], reverse=True):
            name = status_names.get(status, status)
            percentage = (count / len(results)) * 100
            f.write(f"{name}: {count} 個 ({percentage:.1f}%)\n")
        f.write("\n\n")

        # 按狀態分組
        f.write("=" * 70 + "\n")
        f.write("  詳細清單 (按狀態分組)\n")
        f.write("=" * 70 + "\n\n")

        for status in sorted(stats.keys()):
            name = status_names.get(status, status)
            count = stats[status]

            f.write(f"\n{name} ({count} 個)\n")
            f.write("-" * 70 + "\n\n")

            for result in sorted([r for r in results if r['status'] == status], key=lambda x: x['name']):
                f.write(f"檔案: {result['name']}\n")
                f.write(f"  路徑: {result['path']}\n")
                f.write(f"  大小: {format_size(result['size'])}\n")
                f.write(f"  說明: {result['detail']}\n")
                f.write("\n")

    print(f"✅ 文字報告已生成")
    print()

    # 7. 生成人工檢查清單（只包含需要檢查的檔案）
    manual_check_file = '需要人工檢查的檔案.txt'
    print(f"📄 生成人工檢查清單: {manual_check_file}")

    # 需要人工檢查的狀態
    check_statuses = ['ERROR_CORRUPT', 'VALID_ZIP', 'ERROR_STRUCTURE', 'ERROR_UNKNOWN']
    check_files = [r for r in results if r['status'] in check_statuses]

    with open(manual_check_file, 'w', encoding='utf-8') as f:
        f.write("=" * 70 + "\n")
        f.write("  需要人工檢查的檔案清單\n")
        f.write("=" * 70 + "\n\n")

        f.write(f"總數: {len(check_files)} 個檔案\n\n")

        f.write("說明:\n")
        f.write("  這些檔案可能可以修復，建議人工檢查：\n")
        f.write("  1. 用 Excel 打開看看能否開啟\n")
        f.write("  2. 如果能開，另存新檔為 .xlsx 格式\n")
        f.write("  3. 如果不能開，嘗試用 Excel 的「開啟並修復」功能\n\n")
        f.write("-" * 70 + "\n\n")

        for i, result in enumerate(sorted(check_files, key=lambda x: x['name']), 1):
            f.write(f"{i}. {result['name']}\n")
            f.write(f"   路徑: {result['path']}\n")
            f.write(f"   狀態: {status_names.get(result['status'], result['status'])}\n")
            f.write(f"   大小: {format_size(result['size'])}\n")
            f.write(f"   說明: {result['detail']}\n")
            f.write(f"   □ 已檢查\n")  # 複選框供手動勾選
            f.write("\n")

    print(f"✅ 人工檢查清單已生成 ({len(check_files)} 個檔案)")
    print()

    # 8. 總結
    print("=" * 70)
    print("  📋 已生成的檔案")
    print("=" * 70)
    print()
    print(f"1. {csv_file}")
    print("   → 可用 Excel 打開，方便篩選和排序")
    print()
    print(f"2. {txt_file}")
    print("   → 詳細的文字報告，包含所有資訊")
    print()
    print(f"3. {manual_check_file}")
    print("   → 需要人工檢查的 {len(check_files)} 個檔案清單")
    print()

if __name__ == '__main__':
    main()
