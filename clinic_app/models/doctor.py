from basemodel import BaseModel, db


class Doctor(BaseModel):
    __tablename__ = 'doctor'
    area_id = db.Column(db.Integer, db.ForeignKey('area.id'))
    speciality = db.Column(db.String, nullable=False)
    first_name = db.Column(db.String, nullable=False)
    last_name = db.Column(db.String, nullable=False)

    area = db.relationship('Area', back_populates='doctors')

