from clinic_app import ma
from clinic_app.models import Doctor, Patient, FulfilledAppointment, BookedAppointment
from marshmallow import validates, ValidationError


class DoctorSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Doctor
        load_instance = True

    @validates('id')
    def validate_id(self, value):
        if value <= 0:
            raise ValidationError('id must be greater than 0.')


class PatientSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Patient
        load_instance = True


class BookedAppointmentSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = BookedAppointment
        include_fk = True


class FulfilledAppointmentSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = FulfilledAppointment
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
