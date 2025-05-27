from flask import Flask
from flask_cors import CORS
from customer_routes.customer_routes import customer_routes
from dotenv import load_dotenv

load_dotenv()
app = Flask(__name__)
CORS(app)

app.register_blueprint(customer_routes)

@app.route("/")
def home():
    return "Flask + MySQL backend running!"

if __name__ == "__main__":
    app.run(debug=True)



