"""
This module contains all marshmallow schemas for serialization/deserialization of db models,
and some useful functions.

Here are defined The following classes:

- `DoctorSchema`, doctor serialization/deserialization schema
- `PatientSchema`
- `BookedAppointmentSchema`
- `ServedAppointmentSchema`
- `UserSchema`

Functions:

- `paginate_schema`: dynamically defines schema for serialization of flask-SQLAlchemy pagination
- `validate_data`: validate and load data into object using given schema, handling ValidationError
"""

from marshmallow import ValidationError

from clinic_app import ma
from clinic_app.models import Doctor, Patient, ServedAppointment, BookedAppointment, User


class DoctorSchema(ma.SQLAlchemyAutoSchema):
    """
    Doctor serialization/deserialization schema
    """

    class Meta:
        """
        Doctor schema metadata
        """
        load_instance = True
        model = Doctor


class PatientSchema(ma.SQLAlchemyAutoSchema):
    """
    Patient serialization/deserialization schema
    """

    class Meta:
        """
        Patient schema metadata
        """
        load_instance = True
        model = Patient


class BookedAppointmentSchema(ma.SQLAlchemyAutoSchema):
    """
    BookedAppointment serialization/deserialization schema
    """

    class Meta:
        """
        BookedAppointment schema metadata
        """
        model = BookedAppointment
        load_instance = True
        include_fk = True


class ServedAppointmentSchema(ma.SQLAlchemyAutoSchema):
    """
    ServedAppointment serialization/deserialization schema
    """

    class Meta:
        """
        ServedAppointment schema metadata
        """
        model = ServedAppointment
        load_instance = True
        include_fk = True


class UserSchema(ma.SQLAlchemyAutoSchema):
    """
    User serialization/deserialization schema
    """

    class Meta:
        """
        User schema metadata
        """
        model = User
        load_instance = True
        include_fk = True


# pylint: disable=no-member
def pagination_schema(items_schema: ma.Schema):
    """
    Return schema for serialization of flask-SQLAlchemy pagination
    with dynamically defined schema of nested field `items`.

    :param items_schema: schema for Pagination.items
    """

    class PaginationSchema(ma.Schema):
        """Schema for serialization of Pagination object"""
        class Meta:
            """
            Pagination schema metadata
            """
            additional = ('page', 'per_page', 'pages', 'total')

        items = ma.Nested(items_schema, many=True)

    return PaginationSchema


def validate_data(schema: ma.Schema, data, **kwargs):
    """
    Validate data using schema.load(). If validation succeeded return loaded object.

    :param schema: schema for validation
    :param data: data to validate
    :param kwargs: kwargs for passing to Schema.load()
    :return: (loaded_object, None) or (None, error_messages)
    """
    try:
        return schema.load(data, **kwargs), None
    except ValidationError as err:
        return None, err.messages
