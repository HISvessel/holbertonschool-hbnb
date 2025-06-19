"""this is the creation of the file for the amenity entity:
pending further elaboration, since this is for the structure of folders"""
from base_model import BaseClass


class Amenity(BaseClass):
    def __init__(self, amenity_id='', place_id=''):
        super().__init__
        self.amenity_id = amenity_id
        self.place_id = place_id

    def add_to_place(self, place):
        pass