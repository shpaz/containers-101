from flask import Flask
from flask import request, jsonify
from flask_pymongo import PyMongo

app = Flask(__name__)
app.config["MONGO_URI"] = "mongodb://mongodb:27017/movies"
mongo = PyMongo(app)

@app.route("/")
def home():
    return "Welcome to Shon's PoC! nice To Meet You!"
    
@app.route("/list", methods=["GET"])
def list_collection():
    data = mongo.db.fiction.find()
    output = [] 
    for line in data:
      output.append({'name' : line['name']})
    return jsonify({'result': output})
    
if __name__ == "__main__":
    app.run(host='0.0.0.0')
