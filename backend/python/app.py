#hold for back end code- code from chatgpt discussuon wil later alter as needed
# backend/app.py

from flask import Flask, request, jsonify
from database import Database

app = Flask(__name__)
db = Database()  # Initialize your database connection

@app.route('/api/comicbooks', methods=['GET'])
def get_comic_books():
    # Implement logic to fetch comic books from the database
    comic_books = db.get_comic_books()
    return jsonify(comic_books)

# Add routes for other CRUD operations (e.g., create, update, delete)

if __name__ == '__main__':
    app.run(debug=True)
