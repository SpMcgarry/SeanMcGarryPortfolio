#hold for back end code- code from chatgpt discussuon wil later alter as needed
# backend/app.py

from flask import Flask, request, jsonify
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

  

if __name__ == '__main__':
    app.run(debug=True)
