"""
Example app.py app from WSB
"""

from flask import Flask

app = Flask(__name__)


@app.route('/')
def index():
    """ Default controller """
    return '<h1>Hello WSB! Greetings from Flask & Docker!</h1>'


if __name__ == "__main__":
    app.run(debug=True)
