from typing import Optional, List, Union

from pydantic import BaseModel, field_validator

from exceptions.custom_exception import CustomException


class PrimaryContact(BaseModel):
    email: str
    name: str
    gender: str
    msisdn: str
    address: str
    role: Optional[int] = None

    @field_validator('gender')
    def validate_gender(cls, v):
        # Ensure the gender is capitalized
        if v[0].isupper():
            return v
        raise CustomException(message='Gender must be capitalized.')


class SchoolSchema(BaseModel):
    name: str
    msisdn: str
    reg_number: str
    email: str
    country: str
    state: str
    address: str
    primary_contact: PrimaryContact
    logo : str


class SubscribeSchema(BaseModel):
    recurring: bool
    plan_id: int


class UpdateSchoolSchema(BaseModel):
    name: Optional[str] = None
    msisdn: Optional[str] = None
    reg_number: Optional[str] = None
    email: Optional[str] = None
    country: Optional[str] = None
    state: Optional[str] = None
    address: Optional[str] = None
    logo : Optional[str] = None


class ProjectSchema(BaseModel):
    name: str
    description: str
    group_id: List[int]


class UpdateProjectSchema(BaseModel):
    users: Optional[Union[List[int], int]] = None
    group_id: int
    teacher_type: Optional[str] = None


class LearningGroupSchema(BaseModel):
    name: str
    description: str
