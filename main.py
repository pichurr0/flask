from flask import Flask, jsonify
import os

app = Flask(__name__)


@app.route('/')
def index():
    return jsonify({"amor mio":"Esta es la prueba de que la aplicacion puede ser desplegada y que tu la vez desde la casa te amo"})

@app.route('/home')
def index():
    return 'home'

if __name__ == '__main__':
    app.run(debug=True, port=os.getenv("PORT", default=5000))
