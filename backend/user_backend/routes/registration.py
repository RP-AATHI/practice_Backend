from flask import request,jsonify
from controllers.user_controller import save_user_data
import bcrypt
from config.db_config import get_db_connection
from routes.auth_utils import token_required
from flask_bcrypt import Bcrypt

bcrypt = Bcrypt()

def save_user_data(name,user_name ,email, password):
    con = get_db_connection()
    cursor = con.cursor()

    # 🔐 Password ah hash pannu (secret ah convert pannudhu)
    hashed_password = bcrypt.generate_password_hash(password).decode('utf-8')

    query = """
        INSERT INTO users (name ,user_name, email ,password)
        VALUES (%s, %s, %s, %s)
    """
    values = (name,user_name ,email,hashed_password)

    cursor.execute(query, values)
    con.commit()
    cursor.close()
    con.close()

    return {"message": "User registered successfully"}

    # ✅ GET all users
   
def user_crud_routes(app):
    
    @app.route('/users', methods=['GET'])
    def get_all_users():
        con = get_db_connection()
        cursor = con.cursor(dictionary=True)

        cursor.execute("SELECT id, name, user_name,email FROM users")
        users = cursor.fetchall()

        cursor.close()
        con.close()

        return users  # returns list of users

    # ✅ GET single user by ID
    @app.route('/users/<int:id>', methods=['GET'])
    def get_user(id):
        con = get_db_connection()
        cursor = con.cursor(dictionary=True)

        cursor.execute("SELECT id, name,user_name ,email,password FROM users WHERE id = %s", (id,))
        user = cursor.fetchone()

        cursor.close()
        con.close()

        if user:
            return user
        else:
            return {"error": "User not found"}, 404

    # ✅ UPDATE user
    @app.route('/users/<int:id>', methods=['PUT'])
    def update_user(id):
        data = request.get_json()
        name = data.get("name")
        email = data.get("email")

        con = get_db_connection()
        cursor = con.cursor()

        cursor.execute("UPDATE users SET name = %s, email = %s  WHERE id = %s", (name, email,id))
        con.commit()

        cursor.close()
        con.close()

        return {"message": "User updated successfully"}

    # ✅ DELETE user
    @app.route('/users/<int:id>', methods=['DELETE'])
    def delete_user(id):
        con = get_db_connection()
        cursor = con.cursor()

        cursor.execute("DELETE FROM users WHERE id = %s", (id,))
        con.commit()

        cursor.close()
        con.close()

        return {"message": "User deleted successfully"}
    

'''
def user_crud_routes(app):

    # ✅ GET one user by ID (protected)
    @app.route('/user/<int:id>', methods=['GET'])
    @token_required
    def get_user(id):
        con = get_db_connection()
        cursor = con.cursor(dictionary=True)

        cursor.execute("SELECT id, name, email FROM users WHERE id = %s", (id,))
        user = cursor.fetchone()

        cursor.close()
        con.close()

        if user:
            return jsonify(user)
        else:
            return jsonify({"error": "User not found"}), 404

    # ✅ GET all users (protected)
    @app.route('/users', methods=['GET'])
    @token_required
    def get_all_users():
        con = get_db_connection()
        cursor = con.cursor(dictionary=True)

        cursor.execute("SELECT id, name, email FROM users")
        users = cursor.fetchall()

        cursor.close()
        con.close()

        return jsonify(users)

    # ✅ UPDATE user (protected)
    @app.route('/user/<int:id>', methods=['PUT'])
    @token_required
    def update_user(id):
        data = request.get_json()
        name = data.get("name")
        email = data.get("email")

        if not name or not email:
            return jsonify({"error": "Name and Email are required"}), 400

        con = get_db_connection()
        cursor = con.cursor()

        cursor.execute("UPDATE users SET name = %s, email = %s WHERE id = %s", (name, email, id))
        con.commit()

        cursor.close()
        con.close()

        return jsonify({"message": "User updated successfully"})

    # ✅ DELETE user (protected)
    @app.route('/user/<int:id>', methods=['DELETE'])
    @token_required
    def delete_user(id):
        con = get_db_connection()
        cursor = con.cursor()

        cursor.execute("DELETE FROM users WHERE id = %s", (id,))
        con.commit()

        cursor.close()
        con.close()

        return jsonify({"message": "User deleted successfully"})
'''
def register_routes(app):
    @app.route("/register", methods=["POST"])
    def register():
        data = request.get_json()
        name = data.get("name")
        user_name = data.get("user_name")
        email = data.get("email")
        password = data.get("password")
        return save_user_data(name,user_name, email, password)

