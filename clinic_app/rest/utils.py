from marshmallow import ValidationError
from clinic_app import ma


def validate_data(schema: ma.Schema, data, **kwargs):
    """
    Validate data using schema.load().
    :param schema: schema for validation
    :param data: data to validate
    :param kwargs: kwargs for passing to Schema.load()
    :return: (validated_object, None) or (None, error_messages)
    """
    try:
        return schema.load(data, **kwargs), None
    except ValidationError as err:
        return None, err.messages
