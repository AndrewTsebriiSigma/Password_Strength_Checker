from flask import Flask, jsonify, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/api/password', methods=['POST'])
def password():
    data = request.json
    user_input = data.get('input', '')

    response_message = user_input
    return jsonify({'message': response_message})


if __name__ == '__main__':
    app.run(debug=True)