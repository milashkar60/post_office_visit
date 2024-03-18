from flask import Flask, request, jsonify
from flask_cors import CORS
import json
import boto3
import requests


app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*"}})

@app.route('/login', methods=['POST'])
def login():
    # Assuming the POST request contains JSON data with keys 'username' and 'password'
    data = request.json
    username = data.get('username')
    password = data.get('password')

    # Perform authentication logic here
    # For demonstration purposes, let's just return a success message
    if username == 'nurse123' and password == 'password':
        return jsonify({'ok': True})
    else:
        return jsonify({'ok': False}), 401
	
@app.route('/connect', methods=['POST'])
def connectToModel():
	# Connect to model
    url = "https://mgs9tq1g7f.execute-api.us-east-1.amazonaws.com/MellissaStage/Get"  
 
    # Make a GET request
    response = requests.get(url)
 
    # Check if the request was successful (status code 200)
    if response.status_code == 200:
    # Access the response data
        data = response.json()  # Assuming the response is JSON data
        print(data)
    else:
        print("Error:", response.status_code)    
        
    return jsonify({
        'advice': data["body"]
    })
	
if __name__ == '__main__':
    app.run(port=3000)