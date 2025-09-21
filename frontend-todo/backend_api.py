from flask import Flask, request, jsonify
import pymongo

app = Flask(__name__)

# MongoDB Atlas connection
client = pymongo.MongoClient("your_mongodb_atlas_connection_string")
db = client["todoDB"]
collection = db["todoItems"]

@app.route('/submittodoitem', methods=['POST'])
def submit_todo_item():
    try:
        itemName = request.form['itemName']
        itemDescription = request.form['itemDescription']

        collection.insert_one({
            "itemName": itemName,
            "itemDescription": itemDescription
        })
        return jsonify({"message": "Item stored successfully!"}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
