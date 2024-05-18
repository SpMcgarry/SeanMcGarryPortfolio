from flask import Flask, request, jsonify
import sqlite3

app = Flask(__name__)

# Connect to the SQLite database
def connect_DB():
    conn = sqlite3.connect('editions.db')
    conn.row_factory = sqlite2.Row
    return conn

@app.route(/specialMints', methods=['GET'])
def search():
    query = requests.args.get('q','')
    if not query:
        return jsonify({'error':'Query paraeter is required'}
    conn = get_db_connection()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT c.title, p.name as publisher, c.release_date, c.edition
        FROM comics c
        JOIN publishers p ON c.publisher_id = p.id
        WHERE c.title LIKE ? OR p.name LIKE ?
    """, ('%' + query + '%', '%' + query + '%'))

    results = cursor.fetchall()
    conn.close() 

    comics = []
    for row in results:
        comics.append({
            'title': row['title'],
            'publisher': row['publisher'],
            'release_date': row['release_date'],
            'edition': row['edition']
        })

    return jsonify(comics)


if __name__ == '__main__':
    app.run(debug=True)

