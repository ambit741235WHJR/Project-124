# Importing Flask
from flask import Flask, jsonify, request

app = Flask(__name__)
contacts = [
    {
        'id': 1,
        'name': 'John Doe',
        'phone': '555-555-5555',
        'email': '',
        'address': '',
        'done': False
    },
    {        
        'id': 2,
        'name': 'Jane Doe',
        'phone': '555-555-5555',
        'email': '',
        'address': '',
        'done': False
    }
]

@app.route('/')
def index():
    return '<h1>Hello, run the API in the Postman App! Routes are </br> 1. /add-data (POST) </br> 2. /get-data (GET)</h1>'

@app.route('/add-data', methods=['POST'])
def add_data():
    if not request.json:
        return jsonify({'status': 'error', 'message': 'No data received'})
    contact = {
        'id': contacts[-1]['id'] + 1,
        'name': request.json['name'],
        'phone': request.json.get('phone', ""),
        'email': request.json.get('email', ""),
        'address': request.json.get('address', ""),
        'done': False
    }
    contacts.append(contact)
    return jsonify({'status': 'success', 'message': 'Contact added successfully', 'data': contact})

@app.route('/get-data', methods=['GET'])
def get_data():
    return jsonify({'data': contacts})

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0")