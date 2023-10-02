from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return '<h1>Python Operations with Flask Routing and Views</h1>'

@app.route('/print/<string:text>')
def print_text(text):
    print(text)  # Print the text to the console
    return text  # Return plain text instead of HTML

@app.route('/count/<int:number>')
def count(number):
    numbers = '\n'.join(str(i) for i in range(number))
    return numbers  # Return plain text with line breaks

@app.route('/math/<float:num1><string:operation><float:num2>')
def math(num1, operation, num2):
    if operation == '+':
        result = num1 + num2
    elif operation == '-':
        result = num1 - num2
    elif operation == '*':
        result = num1 * num2
    elif operation == 'div':
        if num2 != 0:
            result = num1 / num2
        else:
            return "Division by zero is not allowed."
    elif operation == '%':
        result = num1 % num2
    else:
        return "Invalid operation."
    
    return str(result)

if __name__ == '__main__':
    app.run(port=5555)
