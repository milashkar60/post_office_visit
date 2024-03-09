from flask import Flask, request, jsonify
from flask_cors import CORS


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
    if username == 'admin' and password == 'admin':
        return jsonify({'ok': True})
    else:
        return jsonify({'ok': False}), 401
	
if __name__ == '__main__':
    app.run(port=3000)