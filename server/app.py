#!/usr/bin/env python3

from flask import Flask
import ipdb

app = Flask(__name__)

@app.route('/')
def index():
    return '<h1>Python Operations with Flask Routing and Views</h1>'

@app.route('/print/<string:message>')
def print_string(message):
    print(message)
    return message

@app.route('/count/<int:num>')
def count(num):
    return '\n'.join(str(i) for i in range(num)) + '\n'

@app.route('/math/<int:num1>/<string:operation>/<int:num2>')
def math(num1, operation, num2):
    if operation == '+':
        return str(num1 + num2)
    elif operation == '-':
        return str(num1 - num2)
    elif operation == '*':
        return str(num1 * num2)
    elif operation == 'div':
        return str(num1 / num2)
    elif operation == '%':
        return str(num1 % num2)
    else:
        return 'Error!'

if __name__ == '__main__':
    app.run(port=5555, debug=True)
