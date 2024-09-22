from flask import Flask, request, jsonify
import base64

app = Flask(__name__)

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
        "user_id": "atharv_aras_22092004",  # Use your name and dob
        "email": "your_college_email@example.com",
        "roll_number": "your_college_roll_number",
        "numbers": numbers,
        "alphabets": alphabets,
        "highest_lowercase_alphabet": [highest_lowercase] if highest_lowercase else [],
        "file_valid": file_valid,
        "file_mime_type": file_mime_type,
        "file_size_kb": round(file_size_kb, 2)
    }

    return jsonify(response)

if __name__ == '__main__':
    app.run(debug=True)
