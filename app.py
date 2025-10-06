from flask import Flask, request
app = Flask(__name__)

@app.route('/', methods=['GET'])
def hello():
    return 'Hello World from v-1!\n'
