from flask import Flask, request
app = Flask(__name__)

@app.route('/', methods=['GET'])
def hello():
    who = request.args.get('who', 'Whizlabs')
    return f'Hello {who} from v2!\n'
