from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Allow all origins (for dev)

@app.route('/api/message', methods=['POST'])
def message():
    data = request.get_json()
    name = data.get('name')
    message = f"Vanakkam {name}, Flask irundhu vandha reply!"
    return jsonify({'reply': message})

if __name__ == '__main__':
    app.run(port=5000)
