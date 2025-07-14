"""this is the creation of the file for the amenity entity:
pending further elaboration, since this is for the structure of folders"""
from app.models.base_model import BaseClass
from app.extensions.extensions import db


class Amenity(BaseClass):
    def __init__(self, name=''):
        super().__init__()
        self.name = name

    __tablename__ = 'amenities'
    id = db.Column(db.String, nullable=False) #makes for primary key
    name = db.Column(db.String, nullable=False)

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
