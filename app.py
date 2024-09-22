from flask import Flask, request, jsonify
from flask_cors import CORS  # Import CORS
import base64
import os  # Import the os module

app = Flask(__name__)

# Enable CORS for specific origins
CORS(app, resources={r"/bfhl": {"origins": "http://localhost:3000"}})

# Root endpoint
@app.route('/', methods=['GET'])
def home():
    return jsonify({"message": "Welcome to the API. Use /bfhl for operations."}), 200

# GET request handler
@app.route('/bfhl', methods=['GET'])
def handle_get():
    return jsonify({"operation_code": 1}), 200

# POST request handler
@app.route('/bfhl', methods=['POST'])
def handle_post():
    data = request.json.get('data', [])
    file_b64 = request.json.get('file_b64', "")
    
    # Extract numbers and alphabets
    numbers = [item for item in data if item.isdigit()]
    alphabets = [item for item in data if item.isalpha()]

    # Find highest lowercase alphabet
    lowercase_alphabets = [ch for ch in alphabets if ch.islower()]
    highest_lowercase = max(lowercase_alphabets) if lowercase_alphabets else None

    # File handling
    file_valid = False
    file_mime_type = None
    file_size_kb = 0

    if file_b64:
        try:
            decoded_file = base64.b64decode(file_b64)
            file_size_kb = len(decoded_file) / 1024  # Convert size to KB
            file_valid = True
            file_mime_type = "image/png"  # Hardcoded MIME type for now
        except Exception as e:
            file_valid = False

    response = {
        "is_success": True,
        "user_id": "atharv_aras_22092004",
        "email": "ad9694@srmist.edu.in",
        "roll_number": "RA2111003010655",
        "numbers": numbers,
        "alphabets": alphabets,
        "highest_lowercase_alphabet": [highest_lowercase] if highest_lowercase else [],
        "file_valid": file_valid,
        "file_mime_type": file_mime_type,
        "file_size_kb": round(file_size_kb, 2)
    }

    return jsonify(response)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=int(os.environ.get("PORT", 5000)), debug=True)
