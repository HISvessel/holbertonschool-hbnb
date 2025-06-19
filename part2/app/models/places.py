"""this is the file for the creation of our place entity; changes pending
as this is for file structure"""
from base_model import BaseClass

class Place(BaseClass):
    def __init__(self, title='', description='', owner_id='',
                 latitude=0.0, longitude=0.0, price=0.0):
        super().__init__
        self.title = title
        self.description = description
        self.price = 0
        self.latitude = 0
        self.longitude = 0
        self.owner_id = owner_id
        self.amenities = []
        self.reviews = []

    def add_review(self, review):
        self.reviews.append(review)
    
    def add_amenity(self, amenity):
        self.amenities.append(amenity)