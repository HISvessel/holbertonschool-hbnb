"""this is the creation of the file for the amenity entity:
pending further elaboration, since this is for the structure of folders"""
from base_model import BaseClass


class Amenity(BaseClass):
    def __init__(self, amenity_name=''):
        super().__init__
        self.amenity_name = amenity_name

    def verification(self):
        errors = []
        if not self.amenity_name:
            errors.append("Name for amenity is required")
        return errors

    def to_dict(self):
        data = super().to_dict()
        data.update({
            "same": self.amenity_name
        })
        return data