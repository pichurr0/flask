import os
from flask import Flask, make_response


app = Flask(__name__)

@app.route('/')
def index():
    return make_response({"key":"value"})

if __name__ == '__main__':
    app.run(debug=True, port=os.getenv("PORT", default=5000))
