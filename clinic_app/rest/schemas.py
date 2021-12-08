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
"""

from flask_restful import abort
from marshmallow import ValidationError

from clinic_app import ma
from clinic_app.models import Doctor, Patient, ServedAppointment, BookedAppointment, User


class BaseSchema(ma.SQLAlchemyAutoSchema):
    """Custom base schema class"""

    # pylint: disable=inconsistent-return-statements
    def load_or_422(self, data, **kwargs):
        """
        Return loaded data. If validation error occurs throw 422 http error.

        :param data: data to validate
        :param kwargs: kwargs to Schema.load()
        :return: loaded_object
        """
        try:
            return self.load(data, **kwargs)
        except ValidationError as err:
            abort(422, errors=err.messages, message='Data is invalid')


class DoctorSchema(BaseSchema):
    """
    Doctor serialization/deserialization schema
    """

    class Meta:
        """
        Doctor schema metadata
        """
        load_instance = True
        model = Doctor


class PatientSchema(BaseSchema):
    """
    Patient serialization/deserialization schema
    """

    class Meta:
        """
        Patient schema metadata
        """
        load_instance = True
        model = Patient


class BookedAppointmentSchema(BaseSchema):
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


class ServedAppointmentSchema(BaseSchema):
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

    patient_id = ma.auto_field(required=True)
    doctor_id = ma.auto_field(required=True)


class UserSchema(BaseSchema):
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
