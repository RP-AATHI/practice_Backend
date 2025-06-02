from flask import request, jsonify
from config.db_config import get_db_connection
from routes.auth_utils import token_required

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
