from flask import Flask, request
from operations import add, sub, mult, div

app = Flask(__name__)

# @app.route('/add')
# def add_numbers():
#     a = int(request.args.get('a'))
#     b = int(request.args.get('b'))
#     result = add(a, b)
#     return result

# @app.route('/sub')
# def subtract_numbers():
#     a = int(request.args.get('a'))
#     b = int(request.args.get('b'))
#     result = sub(a, b)
#     return result

# @app.route('/mult')
# def multiply_numbers():
#     a = int(request.args.get('a'))
#     b = int(request.args.get('b'))
#     result = mult(a, b)
#     return result

# @app.route('/div')
# def divide_numbers():
#     a = int(request.args.get('a'))
#     b = int(request.args.get('b'))
#     result = div(a, b)
#     return result

operations = {
    'add': add,
    'sub': sub,
    'mult': mult,
    'div': div
}

@app.route('/<operation>')
def do_math(operation):
    a = int(request.args.get('a'))
    b = int(request.args.get('b'))
    result = operations[operation](a, b)
    return str(result)
    



