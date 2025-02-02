import os
from flask import Flask, jsonify, request
from pymongo import MongoClient

app = Flask(__name__)

client = MongoClient(os.getenv("MONGODB_URI"))
db = client["user_lounge_info"]


@app.route("/level", methods=["GET"])
def get_data():
    try:
        level = request.args.get("l")
        collection = db[f"floor_{level}_lounge_data"]
        data = list(collection.find({}))
        return jsonify(data), 200
    except Exception as e:
        return {"error": e}, 500


if __name__ == "__main__":
    app.run(debug=True)
