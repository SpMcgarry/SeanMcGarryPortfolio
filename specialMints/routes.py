# routes.py
from flask import render_template
from specialMints import app

@app.route('/specialMints')
def index():
    return render_template('index.html')

# Add more routes as needed for your application
# routes.py
from flask import render_template
from specialMints import app

@app.route('/specialMints')  # Define a route for the specialMints page
def special_mints():
    return render_template('index.html')  # Render the index.html template for the specialMints page

