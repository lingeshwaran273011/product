from flask import Flask,request,jsonify
from pymongo import MongoClient
from bson.objectid import ObjectId

app = Flask(__name__)

client = MongoClient("mongodb://localhost:27017")
db = client["product"]
collection = db["item"]

@app.route('/addproduct' ,methods=['POST'])
def approduct():
    data = request.json
    result = collection.insert_one(data)
    return jsonify({'_id':str(result.inserted_id)})

if __name__ == "__main__":
    app.run(debug=True)