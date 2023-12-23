from flask import Flask, request, jsonify
from operations import *

app = Flask(__name__)

@app.route("/")
def greet():
    return "Rise-Back!"


@app.route("/v1/insert", methods = ["POST"])
def insert():
    try:
        first_name = request.json["first_name"]
        last_name = request.json["last_name"]
        address = request.json["address"]
        balance = request.json["balance"]
        add_customer([first_name, last_name, address, balance])
        return f"Custumer {first_name} added to Bank Successfully.", 201

    except Exception as error:
        return f"Could not add Customer because, {error}", 400


@app.route("/v1/retrieve/<string:acc_no>", methods = ["GET"])
def retrieve(acc_no):
    try:
        data = retrieve_data(acc_no)
        if data:
            return jsonify(data)
        else:
            return f"Could not find Customer",404

    except Exception as error:
        return f"Could not retrieve Customer Data because, {error}", 400


@app.route("/v1/update/<string:acc_no>", methods = ["PUT"])
def update(acc_no):
    try:
        first_name = request.json["first_name"]
        last_name = request.json["last_name"]
        address = request.json["address"]
        update_data((first_name, last_name, address, acc_no))
        return f"Customer {first_name}'s Data Updated Successfully.", 201

    except Exception as error:
        return f"Could not update Customer data because, {error}", 400


@app.route("/v1/delete/<string:acc_no>", methods = ["DELETE"])
def delete(acc_no):
    try:
        remove(acc_no)
        return f"Customer with account no : {acc_no} data has been deleted Successfully.", 201

    except Exception as error:
        return f"Could not Delete Customer's data because, {error}", 400


@app.route("/v1/add_money/<string:acc_no>", methods = ["PATCH"])
def add_balance(acc_no):
    try:
        amount = request.json["amount"]
        add_money(acc_no, amount)
        return f"Customer with account no : {acc_no} has been Credited with Rs.{amount}.", 201
    except Exception as error:
        return f"Could not add money because, {error}", 400
        

@app.route("/v1/retrieve_money/<string:acc_no>", methods = ["PATCH"])
def retrieve_balance(acc_no):
    try:
        amount = request.json["amount"]
        retrieve_money(acc_no, amount)
        return f"Customer with account no : {acc_no} has been Debited  with Rs.{amount}.", 201
    except Exception as error:
        return f"Could not add money because, {error}", 400


if __name__ == "__main__":
    app.run(debug=True)