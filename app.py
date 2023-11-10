from flask import Flask, request
from operations import add, sub, mult, div

app = Flask(__name__)

# operations = {
#     'add': add,
#     'sub': sub,
#     'mult': mult,
#     'div': div
# }

# @app.route('/<operation>')
# def do_math(operation):
#     a = int(request.args.get('a'))
#     b = int(request.args.get('b'))
#     result = operations[operation](a, b)
#     return result

@app.route('/add')
def add_numbers():
    a = int(request.args.get('a'))
    b = int(request.args.get('b'))
    result = operations['add'](a, b)
    return result

@app.route('/sub')
def subtract_numbers():
    a = int(request.args.get('a'))
    b = int(request.args.get('b'))
    result = operations['sub'](a, b)
    return result

@app.route('/mult')
def multiply_numbers():
    a = int(request.args.get('a'))
    b = int(request.args.get('b'))
    result = operations['mult'](a, b)
    return result

@app.route('/div')
def divide_numbers():
    a = int(request.args.get('a'))
    b = int(request.args.get('b'))
    result = operations['div'](a, b)
    return result
    



