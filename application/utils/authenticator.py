from functools import wraps

import jwt
from flask import request
from flask_jwt_extended import verify_jwt_in_request, get_current_user

from application import db
from application.Enums.Enums import BasicRoles
from exceptions.custom_exception import CustomException, ExceptionCode


def authenticate():
    def decorator(f):
        @wraps(f)
        def decorated_function(*args, **kwargs):
            try:
                verify_jwt_in_request()
                user = get_current_user()
                if user.isDeactivated:
                    raise CustomException(message="Your account has been deactivated", status_code=400)
                return f(*args, **kwargs)

            except jwt.ExpiredSignatureError:
                raise CustomException(ExceptionCode.EXPIRED_TOKEN)
            except jwt.InvalidTokenError:
                raise CustomException(ExceptionCode.INVALID_TOKEN)

        return decorated_function

    return decorator
