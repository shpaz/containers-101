from flask import Flask
from flask import request, jsonify
from flask_pymongo import PyMongo

app = Flask(__name__)
app.config["MONGO_URI"] = "mongodb://mongodb:27017/containers-101"
mongo = PyMongo(app)

@app.route("/")
def home():
    return "Welcome to Containers 101 course! Nice to meet you!"
    
@app.route("/list", methods=["GET"])
def list_collection():
    data = mongo.db.inventory.find()
    output = [] 
    for line in data:
      line['_id'] = str(line['_id'])
      output.append(line)
    return jsonify({'documents': output})
    
if __name__ == "__main__":
    app.run(host='0.0.0.0')
