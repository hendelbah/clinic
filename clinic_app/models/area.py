from .basemodel import BaseModel, db


class Area(BaseModel):
    __tablename__ = 'area'
    name = db.Column(db.String(60), nullable=False, unique=True)
    description = db.Column(db.String(255))

    doctors = db.relationship('Doctor', back_populates='area')
