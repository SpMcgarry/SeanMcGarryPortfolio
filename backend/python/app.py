from flask import Flask, request, jsonify
import sqlite3

app = Flask(__name__)

# Connect to the SQLite database
conn = sqlite3.connect('sigmintdata.db.sql')
cursor = conn.cursor()

@app.route('/')
def index():
    return open('specialmints.html').read()

@app.route('/specialMints', methods=['GET'])
def search_data():
    # Get the search query from the query parameters
    search_query = request.args.get('search_query')

    # Check if the search query is a number or a name
    try:
        search_value = int(search_query)
        # If it's a number, search for related items in the database
        cursor.execute("SELECT * FROM 'Veve Comics ' WHERE editions = ?", (search_value,))
        results = cursor.fetchall()
        if results:
            search_results = {'items': results}
            return jsonify(search_results)
        else:
            return jsonify({'message': 'No items found related to the given number.'})
    except ValueError:
        # If it's not a number, assume it's a name and search for related numbers and reasons in the database
        cursor.execute("SELECT * FROM 'Veve Comics ' WHERE ItemName LIKE ?", ('%' + search_query + '%',))
        name_results = cursor.fetchall()
        if name_results:
            related_numbers = []
            for item in name_results:
                related_numbers.append({'ItemName': item[2], 'editions': item[4], 'reason': 'Related to the search term'})
            search_results = {'related_numbers': related_numbers}
            return jsonify(search_results)
        else:
            return jsonify({'message': 'No items found related to the given name.'})
    except Exception as e:
        return jsonify({'error': str(e)})
if __name__ == '__main__':
    app.run(debug=True)

