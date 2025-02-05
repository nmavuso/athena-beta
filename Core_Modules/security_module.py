# Core_Modules/security_module.py
import jwt
import datetime

SECRET_KEY = "your-very-secure-secret-key"

def generate_token(user_id):
    """
    Generates a JWT token for the given user.
    """
    payload = {
        'user_id': user_id,
        'exp': datetime.datetime.utcnow() + datetime.timedelta(hours=1)
    }
    token = jwt.encode(payload, SECRET_KEY, algorithm='HS256')
    return token

def verify_token(token):
    """
    Verifies the given JWT token.
    """
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=['HS256'])
        return payload['user_id']
    except Exception as e:
        print(f"Token verification failed: {e}")
        return None
