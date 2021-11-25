from clinic_app import db


class BaseModel(db.Model):
    __abstract__ = True
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)

    def __repr__(self):
        values = [f"{key}={repr(value)}" for key, value in self.as_dict()]
        values_str = ", ".join(values)
        return f"<{self.__class__.__name__}({values_str})>"

    def as_dict(self):
        """
        Iterate over a Model instance, getting tuples of (column_name, value)

        :return: (column_name, value) generator
        """
        for key in self.__table__.columns.keys():
            yield key, self.__getattribute__(key)

    @staticmethod
    def prepare(obj, *, root: str = None):
        """
        Recursively convert given object to serializable form and return result.
        For a list prepare each element in place,
        BaseModel instance is converted to dict,
        any other object stays the same.
        Optionally wrap result with a dict, where key = root, value = result

        :param obj: object for serialization
        :type obj: list | BaseModel
        :param root: key for the result wrapping
        :return: converted object
        :rtype: list | dict
        """
        if root:
            return {root: BaseModel.prepare(obj)}
        if isinstance(obj, BaseModel):
            return dict(obj.as_dict())
        if isinstance(obj, list):
            for i, item in enumerate(obj):
                obj[i] = BaseModel.prepare(item)
            return obj
        return obj

