from flask import Flask
from flask_cors import CORS
from auth_utils import token_required
from routes.registration import register_routes,user_crud_routes
from routes.user_login import login_routes  # later for login

app = Flask(__name__)
CORS(app)

app.config['SECRET_KEY'] = 'HS256'  # secret for signing token
# Register routes
register_routes(app)
user_crud_routes(app)
login_routes(app)  # only after you create this

if __name__ == "__main__":
    app.run(debug=True)

