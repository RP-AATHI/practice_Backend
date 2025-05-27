# from flask import Blueprint, request, jsonify
# from controllers.user_controller import save_user_data

# user_routes = Blueprint('user_routes', __name__)

# @user_routes.route('/register', methods=['POST'])
# def register():
#     data = request.json
#     save_user_data(data)  # send to controller
#     return jsonify({'message': 'User registered successfully', 'data': data})
# routes/user_routes.py

from flask import Blueprint, request, jsonify
from controllers.user_controller import save_user_data

user_routes = Blueprint("user_routes", __name__)

@user_routes.route("/register", methods=["POST"])
def register_user():
    data = request.get_json()
    name = data.get("name")
    email = data.get("email")
    
    if not name or not email:
        return jsonify({"error": "Name and email required"}), 400

    result = save_user_data(name, email)
    return jsonify(result)
