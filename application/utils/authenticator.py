from functools import wraps
import inspect
from typing import get_origin, Union, get_args

import jwt
from flask import request
from flask_jwt_extended import verify_jwt_in_request, get_current_user

from application import db, return_json, OutputObj
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


def required_arguments_exist(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        signature = inspect.signature(f)
        bound_parameters = signature.bind_partial(*args, **kwargs)
        bound_parameters.apply_defaults()

        for name, value in bound_parameters.arguments.items():

            if name not in 'cls':

                if value is None:
                    raise CustomException(message=f"Parameter {name} is required", status_code=400)

                expected_type = signature.parameters[name].annotation
                origin = get_origin(expected_type)

                if origin is Union:
                    if not any(isinstance(value, t) for t in get_args(expected_type)):
                        raise CustomException(message=f"Parameter {name} should be a {get_args(expected_type)}", status_code=400)

                elif not isinstance(value, signature.parameters[name].annotation):
                    raise CustomException(message=f"Parameter {name} should be a {signature.parameters[name].annotation}", status_code=400)

        return f(*args, **kwargs)

    return decorated_function


def response_decorator(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        result = f(*args, **kwargs)
        message = isinstance(result, str)
        return return_json(OutputObj(data=result if not message else None, message=result if message else "Data Fetched"))

    return decorated_function


def is_admin():
    def decorator(f):
        @wraps(f)
        def decorated_function(*args, **kwargs):
            user = get_current_user()
            if not user.is_admin:
                raise CustomException(ExceptionCode.ADMIN_ACCESS_REQUIRED)
            return f(*args, **kwargs)

        return decorated_function

    return decorator
