from flask import Flask, jsonify, request


app = Flask(__name__)
PORT = 3000


@app.route('/sumar', methods=['POST'])
def Suma():
    request_data = request.get_json()
    return sumar(request_data['num1'], request_data['num2'])


def sumar(num1: int, num2: int):
    result = num1+num2
    return jsonify({'Resultado': result})


@app.route('/restar', methods=['POST'])
def Resta():
    request_data = request.get_json()
    return restar(request_data['num1'], request_data['num2'])


def restar(num1: int, num2: int):
    result = num1-num2
    return jsonify({'Resultado': result})


@app.route('/multiplicar', methods=['POST'])
def Multiplica():
    request_data = request.get_json()
    return multiplicar(request_data['num1'], request_data['num2'])


def multiplicar(num1: int, num2: int):
    result = num1*num2
    return jsonify({'Resultado': result})


if __name__ == '__main__':
    # run app in debug mode on port 3000
    app.run(debug=True, port=PORT)
