'''
import jwt
from flask import request, jsonify, current_app

def token_required(f):
    def wrapper(*args, **kwargs):
        token = None
        if 'Authorization' in request.headers:
            token = request.headers['Authorization'].split(" ")[1]

        if not token:
            return jsonify({'error': 'Token missing'}), 401

        try:
            data = jwt.decode(token, current_app.config['SECRET_KEY'], algorithms=['HS256'])
            request.user_id = data['user_id']
        except jwt.ExpiredSignatureError:
            return jsonify({'error': 'Token expired'}), 401
        except jwt.InvalidTokenError:
            return jsonify({'error': 'Invalid token'}), 401

        return f(*args, **kwargs)
    wrapper.__name__ = f.__name__
    return wrapper
'''

# import jwt
# import datetime
# from flask import request, jsonify, current_app

# def token_required(f):
#     def wrapper(*args, **kwargs):
#         token = None
#         if 'Authorization' in request.headers:
#             token = request.headers['Authorization'].split(" ")[1]

#         if not token:
#             return jsonify({'error': 'Token missing'}), 401

#         try:
#             data = jwt.decode(token, current_app.config['SECRET_KEY'], algorithms=['HS256'])
#             request.user_id = data['user_id']
#         except jwt.ExpiredSignatureError:
#             return jsonify({'error': 'Token expired'}), 401
#         except jwt.InvalidTokenError:
#             return jsonify({'error': 'Invalid token'}), 401

#         return f(*args, **kwargs)
#     wrapper.__name__ = f.__name__
#     return wrapper
#     # Inside auth_utils.py
# print("✅ auth_utils module loaded!")
#----------------------------------------------------------------------------------
import jwt
import datetime
from flask import request, jsonify
from functools import wraps

SECRET_KEY = 'your_secret_key'  # 🔑 Use .env or secure this key

# ✅ Generate JWT Token with Expiry
def generate_token(user_id):
    payload = {
        'user_id': user_id,
        'exp': datetime.datetime.utcnow() + datetime.timedelta(hours=1)  # token valid for 1 hour
    }
    token = jwt.encode(payload, SECRET_KEY, algorithm='HS256')
    return token

# ✅ Middleware – Protect routes using this decorator
def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = None

        # ✅ Token from header
        if 'Authorization' in request.headers:
            auth_header = request.headers['Authorization']
            if auth_header.startswith('Bearer '):
                token = auth_header.split(' ')[1]

        if not token:
            return jsonify({'message': 'Token is missing'}), 401

        try:
            # ✅ Decode & check expiry
            payload = jwt.decode(token, SECRET_KEY, algorithms=['HS256'])
            current_user_id = payload['user_id']
        except jwt.ExpiredSignatureError:
            return jsonify({'message': 'Token has expired. Please login again.'}), 401
        except jwt.InvalidTokenError:
            return jsonify({'message': 'Invalid token'}), 401

        return f(current_user_id, *args, **kwargs)

    return decorated
