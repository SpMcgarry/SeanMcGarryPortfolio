from flask import Flask, request, jsonify
<<<<<<< HEAD
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
=======
from database import Database
import sqlite3
from app.py import userInput

app = Flask(__name__)

conn = sqlite3.connect('sigmintdata.db.sql') #db initialised ()
cursor = conn.cursor()

@app.route('/specialMints', methods=['GET'])
#created database , linked it now to #get the user #search data and conver #to sql querie variable 

def search_data():
  userInput = request.args.get('searchInput')
  
  cursor.execute("SELECT * FROM your_table WHERE your_column LIKE ?", ('%' + userInput + '%',))
  # Fetch the search results
  search_results = cursor.fetchall()

  # Close the cursor and connection
  cursor.close()
  conn.close()

  # Convert the search results to JSON format and return them
  return jsonify(search_results)

  
>>>>>>> 27cf07f (commit test from replit)

if __name__ == '__main__':
    app.run(debug=True)

