# app.py
from flask import Flask, request


app = Flask(__name__)

@app.route('/hello', methods=['GET'])
def index():
    if request.method == 'GET':
        return app.response_class(
        response="Hello, I am the API service!",
        status=200,
    ) 

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080, debug=True, threaded=True)