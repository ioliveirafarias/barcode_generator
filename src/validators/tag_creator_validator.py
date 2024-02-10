from cerberus import Validator
from src.errors.error_types.http_unprocessable_entity import HttpUnprocessableEntityError

def tag_creator_validator(request: any) -> None:
    valid_estructure = {"product_code": {"type": "string", "required": True, "empty": False}}
    body_validator = Validator(valid_estructure)
    response = body_validator.validate(request.json)
    if response is False:
        raise HttpUnprocessableEntityError(body_validator.errors)
