from flask import Flask, jsonify, request


app = Flask(__name__)


incomes = [
    {"description": "salary", "amount": 500}
]


@app.route("/incomes")
def hello_world():
    return jsonify(incomes)


@app.route("/incomes", methods=["POST"])
def add_income():
    incomes.append(request.get_json())
    
    return "", 204