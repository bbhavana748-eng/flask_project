from flask import Flask, jsonify, request, redirect, url_for, render_template
from pymongo import MongoClient
import json

app = Flask(__name__)

# Replace with your MongoDB Atlas URL
client = MongoClient("YOUR_MONGODB_ATLAS_URL")
db = client['testdb']
collection = db['users']

@app.route('/api')
def get_data():
    with open('data.json') as f:
        data = json.load(f)
    return jsonify(data)
@app.route('/', methods=['GET', 'POST'])
def form():
    if request.method == 'POST':
        return redirect(url_for('success'))
    return render_template('form.html')

@app.route('/success')
def success():
    return "Data submitted successfully"

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=10000)
