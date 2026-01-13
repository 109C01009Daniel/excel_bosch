#!/usr/bin/env python3
"""
SQLite 資料庫網頁查看器
類似 phpMyAdmin 的簡單介面
"""
from flask import Flask, render_template, request, jsonify
import sqlite3
from config import DATABASE_PATH
import os

app = Flask(__name__)


def get_db_connection():
    """獲取資料庫連接"""
    conn = sqlite3.connect(DATABASE_PATH)
    conn.row_factory = sqlite3.Row
    return conn


@app.route('/')
def index():
    """首頁 - 顯示資料庫總覽"""
    conn = get_db_connection()
    cursor = conn.cursor()

    # 獲取所有表
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table' ORDER BY name")
    tables = [row[0] for row in cursor.fetchall()]

    # 獲取每個表的記錄數
    table_info = []
    for table in tables:
        if not table.startswith('sqlite_') and not table.startswith('content_fts'):
            try:
                cursor.execute(f"SELECT COUNT(*) FROM {table}")
                count = cursor.fetchone()[0]
                table_info.append({
                    'name': table,
                    'count': count
                })
            except:
                pass

    # 獲取統計資訊
    stats = {
        'db_path': DATABASE_PATH,
        'db_size': os.path.getsize(DATABASE_PATH) / 1024 / 1024,  # MB
    }

    conn.close()

    return render_template('db_viewer.html', tables=table_info, stats=stats)


@app.route('/table/<table_name>')
def view_table(table_name):
    """查看表內容"""
    page = request.args.get('page', 1, type=int)
    per_page = 50
    offset = (page - 1) * per_page

    conn = get_db_connection()
    cursor = conn.cursor()

    # 獲取表結構
    cursor.execute(f"PRAGMA table_info({table_name})")
    columns = [row['name'] for row in cursor.fetchall()]

    # 獲取總記錄數
    cursor.execute(f"SELECT COUNT(*) FROM {table_name}")
    total_count = cursor.fetchone()[0]

    # 獲取資料
    cursor.execute(f"SELECT * FROM {table_name} LIMIT ? OFFSET ?", (per_page, offset))
    rows = cursor.fetchall()

    conn.close()

    return render_template('table_view.html',
                         table_name=table_name,
                         columns=columns,
                         rows=rows,
                         page=page,
                         per_page=per_page,
                         total_count=total_count)


@app.route('/query', methods=['GET', 'POST'])
def query():
    """執行 SQL 查詢"""
    if request.method == 'POST':
        sql = request.form.get('sql', '')

        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute(sql)

            if sql.strip().upper().startswith('SELECT'):
                columns = [description[0] for description in cursor.description]
                rows = cursor.fetchall()
                result = {
                    'success': True,
                    'columns': columns,
                    'rows': [dict(row) for row in rows],
                    'count': len(rows)
                }
            else:
                conn.commit()
                result = {
                    'success': True,
                    'message': 'Query executed successfully',
                    'affected_rows': cursor.rowcount
                }

            conn.close()
            return jsonify(result)

        except Exception as e:
            return jsonify({
                'success': False,
                'error': str(e)
            })

    return render_template('query.html')


@app.route('/api/search')
def api_search():
    """搜索 API"""
    keyword = request.args.get('keyword', '')
    limit = request.args.get('limit', 20, type=int)

    if not keyword:
        return jsonify({'success': False, 'error': 'Keyword is required'})

    conn = get_db_connection()
    cursor = conn.cursor()

    cursor.execute('''
        SELECT
            f.file_name,
            c.sheet_name,
            c.cell_location,
            c.value,
            c.row_num,
            c.col_num
        FROM cells c
        JOIN files f ON c.file_id = f.file_id
        WHERE c.value_lower LIKE ?
        ORDER BY f.file_name, c.sheet_name, c.row_num, c.col_num
        LIMIT ?
    ''', (f'%{keyword.lower()}%', limit))

    results = [dict(row) for row in cursor.fetchall()]
    conn.close()

    return jsonify({
        'success': True,
        'keyword': keyword,
        'count': len(results),
        'results': results
    })


if __name__ == '__main__':
    print("=" * 70)
    print("  📊 SQLite 資料庫查看器")
    print("=" * 70)
    print()
    print(f"  資料庫: {DATABASE_PATH}")
    print(f"  網址: http://localhost:5000")
    print()
    print("  功能:")
    print("    - 查看所有資料表")
    print("    - 瀏覽表內容")
    print("    - 執行 SQL 查詢")
    print("    - 搜索資料")
    print()
    print("  按 Ctrl+C 停止")
    print("=" * 70)
    print()

    app.run(host='0.0.0.0', port=5000, debug=True)
