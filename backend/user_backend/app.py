# from flask import Flask
# from routes.user_routes import user_routes
# from flask_cors import CORS
# from dotenv import load_dotenv

# load_dotenv()

# app = Flask(__name__)
# CORS(app)
# @app.route("/")
# def home():
#     return "Backend working perfectly!"
# @app.route("/register", methods=["POST"])
# def register():
#     return "User registered!"
# # Register the route group (Blueprint)
# app.register_blueprint(user_routes)

# if __name__ == '__main__':
#     app.run(debug=True)

# app.py
#-----------------------------------------------------------------------------------------------
# from flask import Flask
# from routes.user_routes import user_routes
# from flask_cors import CORS
# from dotenv import load_dotenv
# import os

# load_dotenv()

# app = Flask(__name__)
# CORS(app)

# app.register_blueprint(user_routes)

# @app.route("/")
# def home():
#     return "Flask + MySQL backend running!"

# if __name__ == "__main__":
#     app.run(debug=True)
#--------------------------------------------------------------------------------------------------

from flask import Flask
from routes.registration import register_routes,user_crud_routes
from routes.user_login import login_routes  # later for login

app = Flask(__name__)

# Register routes
register_routes(app)
user_crud_routes(app)
login_routes(app)  # only after you create this

if __name__ == "__main__":
    app.run(debug=True)