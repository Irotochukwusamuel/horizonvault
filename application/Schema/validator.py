from typing import Type

from pydantic import BaseModel, ValidationError
from exceptions.custom_exception import CustomException


def validate_data(model: Type[BaseModel], data: dict):
    try:
        validated_data = model(**data)  # noqa
        return validated_data
    except ValidationError as e:
        # Handle the validation error, raise an exception, or perform error handling logic
        raise CustomException(message=e.errors(), status_code=400)


