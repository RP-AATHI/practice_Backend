from flask import Blueprint, request, jsonify
from config.db_config import get_db_connection
from flask_bcrypt import Bcrypt

bcrypt = Bcrypt()

def login_routes(app):
    @app.route('/login', methods=['POST'])
    def login():
        data = request.get_json()
        user_name = data.get('user_name')
        password = data.get('password')

        con = get_db_connection()
        cursor = con.cursor(dictionary=True)

        query = "SELECT * FROM users WHERE user_name = %s"
        cursor.execute(query, (user_name,))
        user = cursor.fetchone()

        cursor.close()
        con.close()

        if user and bcrypt.check_password_hash(user['password'], password):
            return {
                "message": "Login successful",
                "user": {
                    "user_name": user['user_name'],
                    "email": user['email']
                }
            }
        else:
            return {"error": "Invalid email or password"}, 401
