"""
    Program => Present scraped StatArea data in a RESTful API
    Author => Samuel Afolaranmi
    Date => 01-04-2018
"""
from flask import Flask, jsonify
from scrape import main

app = Flask(__name__)


@app.route('/')
def index():
    """
    Present the data in a RESTful API
    """
    return jsonify(main())


if __name__ == "__main__":
    app.run(debug=True, host='127.0.0.1', port=5000)
