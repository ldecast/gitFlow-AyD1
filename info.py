from flask import Flask, jsonify


app = Flask(__name__)
PORT = 4000


@app.route('/', methods=['GET'])
def getInfo():
    return jsonify({'Nombre': 'Luis Danniel Ernesto Castellanos Galindo', 'Carnet': 201902238})


if __name__ == '__main__':
    # run app in debug mode on port 4000
    app.run(debug=True, port=PORT)
