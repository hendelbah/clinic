from clinic_app import db


class BasicQueryHelper:
    db = db

    def __init__(self, model: db.Model):
        self.model = model

    def get_or_404(self, id_: int):
        return self.model.query.filter(self.model.id == id_).first_or_404()

    def exists(self, id_: int):
        exists = self.model.query.filter(self.model.id == id_).exists()
        return self.db.session.query(exists).scalar()

    def get_paginated(self, page: int = None, per_page: int = None):
        return self.model.query.order_by(self.model.id).paginate(page, per_page)

    def commit(self):
        self.db.session.commit()

    def save(self, model: db.Model):
        self.db.session.add(model)
        self.commit()
        return model.id

    def delete(self, id_: int):
        res = self.model.query.filter(self.model.id == id_).delete()
        self.commit()
        return res
