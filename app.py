from flask import Flask, jsonify

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World!'


@app.route('/top/all/query')
def query_all_top():
    pass


if __name__ == '__main__':
    app.run()
