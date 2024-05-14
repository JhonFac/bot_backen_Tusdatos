from functools import wraps

from flask_jwt_extended import get_jwt_identity
from werkzeug.exceptions import Forbidden


def role_required(*allowed_roles):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            user_role = get_jwt_identity()  # Asumiendo que el JWT contiene el rol del usuario
            if user_role in allowed_roles:
                return func(*args, **kwargs)
            else:
                raise Forbidden("You do not have the necessary permissions.")
        return wrapper
    return decorator
