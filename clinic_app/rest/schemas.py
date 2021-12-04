from clinic_app import ma
from marshmallow import validates, ValidationError
from clinic_app.models import Doctor, Patient, FulfilledAppointment, BookedAppointment


class BaseSchema(ma.SQLAlchemyAutoSchema):
    @validates('id')
    def validate_id(self, value):
        if value <= 0:
            raise ValidationError('id must be greater than 0.')


class DoctorSchema(BaseSchema):
    class Meta:
        load_instance = True
        model = Doctor


class PatientSchema(BaseSchema):
    class Meta:
        load_instance = True
        model = Patient


class BookedAppointmentSchema(BaseSchema):
    class Meta:
        model = BookedAppointment
        load_instance = True
        include_fk = True


class FulfilledAppointmentSchema(BaseSchema):
    class Meta:
        model = FulfilledAppointment
        load_instance = True
        include_fk = True


def paginate_schema(items_schema: ma.Schema):
    """
    Return schema for flask-SQLAlchemy pagination with dynamically defined nested schema of items.

    :param items_schema: schema for Pagination.items
    """

    class PaginateSchema(ma.Schema):
        class Meta:
            additional = ('page', 'per_page', 'pages', 'total')

        items = ma.Nested(items_schema, many=True)

    return PaginateSchema


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


__all__ = [DoctorSchema, PatientSchema, BookedAppointmentSchema,
           FulfilledAppointmentSchema, paginate_schema, validate_data]
