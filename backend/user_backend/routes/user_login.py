import jwt
import datetime
import random
from flask import request, jsonify,session
from config.db_config import get_db_connection
from routes.auth_utils import token_required
from flask_bcrypt import Bcrypt
import smtplib
from email.mime.text import MIMEText

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
            token = jwt.encode({
                'user_id': user['id'],
                'exp': datetime.datetime.utcnow() + datetime.timedelta(hours=1)
            }, app.config['SECRET_KEY'], algorithm='HS256')

            return jsonify({
                'message': 'Login successful',
                'token': token
            })
        else:
            return jsonify({'error': 'Invalid credentials'}), 401
#--------------------------------------------------------------------------------------------------
# from flask import Blueprint, request, jsonify, session
# from config.db_config import get_db_connection
# from flask_bcrypt import Bcrypt
# import random
# import smtplib
# from email.mime.text import MIMEText
# import os

# bcrypt = Bcrypt()

# # OTP generator
# def generate_otp():
#     return str(random.randint(100000, 999999))

# # OTP sender
# def send_otp_email(receiver_email, otp):
#     #print(f"[DEBUG] OTP for {receiver_email} is:{otp}")
#     sender_email = os.getenv('EMAIL_USER')  # Example: 'yourname@gmail.com'
#     sender_password = os.getenv('EMAIL_PASS')  # Example: 'your-app-password'

#     msg = MIMEText(f"Your OTP is: {otp}")
#     msg["Subject"] = "OTP for Login Verification"
#     msg["From"] = sender_email
#     msg["To"] = receiver_email

#     try:
#         server = smtplib.SMTP("smtp.gmail.com", 587)
#         server.starttls()
#         server.login(sender_email, sender_password)
#         server.send_message(msg)
#         server.quit()
#     except Exception as e:
#         print("Email send error:", e)

# def login_routes(app):
#     @app.route('/login', methods=['POST'])
#     def login():
#         data = request.get_json()
#         user_name = data.get('user_name')
#         password = data.get('password')

#         con = get_db_connection()
#         cursor = con.cursor(dictionary=True)

#         query = "SELECT * FROM users WHERE user_name = %s"
#         cursor.execute(query, (user_name,))
#         user = cursor.fetchone()

#         cursor.close()
#         con.close()

#         if user and bcrypt.check_password_hash(user['password'], password):
#             otp = generate_otp()
#             session['otp'] = otp
#             session['user_email'] = user['email']
#             session['user_name'] = user['user_name']

#             send_otp_email(user['email'], otp)

#             return jsonify({"message": "OTP sent to your email. Please verify to complete login."})
#         else:
#             return jsonify({"error": "Invalid username or password"}), 401

#     @app.route('/verify-otp', methods=['POST'])
#     def verify_otp():
#         data = request.get_json()
#         input_otp = data.get('otp')

#         if input_otp == session.get('otp'):
#             # Login success
#             user_name = session.get('user_name')
#             email = session.get('user_email')

#             # Clear OTP session
#             session.pop('otp', None)

#             return jsonify({
#                 "message": "Login successful",
#                 "user": {
#                     "user_name": user_name,
#                     "email": email
#                 }
#             })
#         else:
#             return jsonify({"error": "Invalid OTP"}), 401
#---------------------------------------------------------------------------------------------------
# from flask import request
# from flask_bcrypt import Bcrypt
# from config.db_config import get_db_connection

# bcrypt = Bcrypt()

# def login_routes(app):
#     @app.route('/login', methods=['POST'])
#     def login():
#         data = request.get_json()
#         email = data.get('email')
#         password = data.get('password')

#         con = get_db_connection()
#         cursor = con.cursor(dictionary=True)

#         query = "SELECT * FROM users WHERE email = %s"
#         cursor.execute(query, (email,))
#         user = cursor.fetchone()

#         cursor.close()
#         con.close()

#         if user and bcrypt.check_password_hash(user['password'], password):
#             return {
#                 "message": "Login successful",
#                 "user": {
#                     "name": user['name'],
#                     "email": user['email']
#                 }
#             }
#         else:
#             return {"error": "Invalid email or password"}, 401
