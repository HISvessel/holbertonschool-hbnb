"""this is the creation of the file for the amenity entity:
pending further elaboration, since this is for the structure of folders"""
from app.models.base_model import BaseClass


class Amenity(BaseClass):
    def __init__(self, name=''):
        super().__init__()
        self.name = name

    def validate(self):
        errors = []
        if not self.name:
            errors.append("Name for amenity is required")
        return errors

    def to_dict(self):
        data = super().to_dict()
        data.update({
            "name": self.name
        })
        return data