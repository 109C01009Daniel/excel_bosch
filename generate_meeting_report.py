#!/usr/bin/env python3
"""
生成會議用的損壞檔案報告
"""
import os
from collections import defaultdict

def main():
    print("=" * 70)
    print("  📋 生成會議報告")
    print("=" * 70)
    print()

    # 從 CSV 讀取損壞檔案
    corrupted_files = []

    with open('完整檔案狀態清單.csv', 'r', encoding='utf-8-sig') as f:
        lines = f.readlines()[1:]  # 跳過標題

        for line in lines:
            if '🔴 ZIP 損壞' in line:
                parts = line.strip().split('","')
                if len(parts) >= 5:
                    status = parts[0].replace('"', '')
                    filename = parts[1]
                    filepath = parts[2]
                    filesize = parts[3]

                    corrupted_files.append({
                        'name': filename,
                        'path': filepath,
                        'size': filesize
                    })

    print(f"找到 {len(corrupted_files)} 個損壞檔案")
    print()

    # 按目錄分組
    by_directory = defaultdict(list)
    for file_info in corrupted_files:
        # 提取目錄路徑
        path = file_info['path']
        # 移除 /var/www/html/excel_Bosch/Sharepoint/
        relative_path = path.replace('/var/www/html/excel_Bosch/Sharepoint/', '')

        # 提取專案名稱和主要目錄
        parts = relative_path.split('/')
        if len(parts) >= 2:
            project = parts[0]  # Deneb - Documents 或 Hibiscus2 - Documents
            main_dir = parts[1] if len(parts) > 1 else ''
            category = f"{project}/{main_dir}"
        else:
            category = "其他"

        by_directory[category].append(file_info)

    # 生成 Markdown 報告（適合會議投影）
    md_file = 'ZIP損壞檔案報告_會議用.md'
    with open(md_file, 'w', encoding='utf-8') as f:
        f.write("# ZIP 損壞檔案報告\n\n")
        f.write(f"**報告日期**: 2026-01-07\n\n")
        f.write(f"**總損壞檔案數**: {len(corrupted_files)} 個\n\n")

        f.write("---\n\n")
        f.write("## 摘要\n\n")
        f.write("索引過程中發現 113 個 Excel 檔案的 ZIP 結構損壞，無法正常開啟。\n\n")
        f.write("**問題描述**:\n")
        f.write("- ZIP 檔案缺少結尾標記（End-of-central-directory signature）\n")
        f.write("- 可能原因：Sharepoint 同步未完成、網路傳輸中斷、檔案下載不完整\n\n")

        f.write("**影響**:\n")
        f.write("- 這些檔案無法被索引\n")
        f.write("- Python、Excel、LibreOffice 均無法開啟\n")
        f.write("- 需要從 Sharepoint 重新下載\n\n")

        f.write("---\n\n")
        f.write("## 按目錄分類\n\n")

        # 按目錄排序
        for category in sorted(by_directory.keys()):
            files = by_directory[category]
            f.write(f"### {category}\n\n")
            f.write(f"**數量**: {len(files)} 個檔案\n\n")

            for i, file_info in enumerate(sorted(files, key=lambda x: x['name']), 1):
                f.write(f"{i}. **{file_info['name']}**\n")
                f.write(f"   - 大小: {file_info['size']}\n")
                f.write(f"   - 路徑: `{file_info['path']}`\n\n")

        f.write("---\n\n")
        f.write("## 建議處理方式\n\n")
        f.write("1. **短期**: 使用已成功索引的 186 個檔案（56% 覆蓋率）\n")
        f.write("2. **中期**: 從 Sharepoint 重新同步這 113 個檔案\n")
        f.write("3. **長期**: 檢查 Sharepoint 同步設定，避免未來再次發生\n\n")

    print(f"✅ Markdown 報告已生成: {md_file}")

    # 生成簡潔的文字清單（方便複製貼上）
    txt_file = 'ZIP損壞檔案清單_簡潔版.txt'
    with open(txt_file, 'w', encoding='utf-8') as f:
        f.write("=" * 70 + "\n")
        f.write("  ZIP 損壞檔案清單（共 113 個）\n")
        f.write("=" * 70 + "\n\n")

        for i, file_info in enumerate(sorted(corrupted_files, key=lambda x: x['name']), 1):
            f.write(f"{i:3d}. {file_info['name']}\n")
            f.write(f"      {file_info['path']}\n")
            f.write(f"      大小: {file_info['size']}\n\n")

    print(f"✅ 簡潔清單已生成: {txt_file}")

    # 生成 Excel 匯報用的 CSV
    csv_file = 'ZIP損壞檔案清單_匯報用.csv'
    with open(csv_file, 'w', encoding='utf-8-sig') as f:
        f.write("編號,檔案名稱,所屬目錄,檔案大小,完整路徑\n")

        for i, file_info in enumerate(sorted(corrupted_files, key=lambda x: x['name']), 1):
            # 提取目錄
            path = file_info['path']
            relative_path = path.replace('/var/www/html/excel_Bosch/Sharepoint/', '')
            parts = relative_path.split('/')
            if len(parts) >= 2:
                directory = f"{parts[0]}/{parts[1]}"
            else:
                directory = "其他"

            f.write(f'{i},')
            f.write(f'"{file_info["name"]}",')
            f.write(f'"{directory}",')
            f.write(f'"{file_info["size"]}",')
            f.write(f'"{file_info["path"]}"\n')

    print(f"✅ CSV 匯報檔已生成: {csv_file}")

    # 生成統計摘要
    summary_file = 'ZIP損壞檔案統計摘要.txt'
    with open(summary_file, 'w', encoding='utf-8') as f:
        f.write("=" * 70 + "\n")
        f.write("  ZIP 損壞檔案統計摘要\n")
        f.write("=" * 70 + "\n\n")

        f.write(f"總損壞檔案數: {len(corrupted_files)} 個\n\n")

        f.write("按目錄分類:\n")
        f.write("-" * 70 + "\n")
        for category in sorted(by_directory.keys(), key=lambda x: len(by_directory[x]), reverse=True):
            count = len(by_directory[category])
            percentage = (count / len(corrupted_files)) * 100
            f.write(f"{category:50s} {count:3d} 個 ({percentage:5.1f}%)\n")

        f.write("\n")
        f.write("=" * 70 + "\n")
        f.write("  整體索引狀態\n")
        f.write("=" * 70 + "\n\n")

        f.write("總 Excel 檔案數:     332 個\n")
        f.write("成功索引:           186 個 (56.0%)\n")
        f.write("ZIP 損壞:           113 個 (34.0%)\n")
        f.write(".xls 舊格式:         33 個 (10.0%)\n\n")

        f.write("已索引單元格數:   2,432,059 個\n")
        f.write("資料庫大小:       478.11 MB\n\n")

    print(f"✅ 統計摘要已生成: {summary_file}")
    print()

    # 顯示統計
    print("=" * 70)
    print("  📊 損壞檔案統計")
    print("=" * 70)
    print()

    for category in sorted(by_directory.keys(), key=lambda x: len(by_directory[x]), reverse=True):
        count = len(by_directory[category])
        percentage = (count / len(corrupted_files)) * 100
        print(f"{category:50s} {count:3d} 個 ({percentage:5.1f}%)")

    print()
    print("=" * 70)
    print("  📋 已生成的報告檔案")
    print("=" * 70)
    print()
    print(f"1. {md_file}")
    print("   → 會議用 Markdown 報告（可轉 PDF）")
    print()
    print(f"2. {csv_file}")
    print("   → Excel 可開啟的 CSV 檔案")
    print()
    print(f"3. {txt_file}")
    print("   → 完整清單（文字格式）")
    print()
    print(f"4. {summary_file}")
    print("   → 統計摘要")
    print()

if __name__ == '__main__':
    main()
