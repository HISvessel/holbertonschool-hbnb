"""this is the file for the creation of our place entity; changes pending
as this is for file structure"""
from base_model import BaseClass

class Place(BaseClass):
    def __init__(self, title='', description='', owner_id='',
                 latitude=0.0, longitude=0.0, price=0.0):
        super().__init__()
        self.title = title
        self.description = description
        self._price = 0
        self._latitude = 0
        self._longitude = 0
        self.owner_id = owner_id
        self.amenities = []
        self.reviews = []

        self.price = price
        self.latitude = latitude
        self.longitude = longitude
    
    @property
    def price(self):
        return self._price
    
    @price.setter
    def price(self, value):
        try:
            value = float(value)
        except (TypeError, ValueError):
            raise TypeError("Price must be a number")
        if value < 0:
            raise ValueError("Price must not be less than 0")
        self._price = value
    
    @property
    def latitude(self):
        return self._latitude
    
    @latitude.setter
    def latitude(self, point_y):
        try:
            point_y = float(point_y)
        except(ValueError, TypeError):
            raise TypeError("Latitude must be float")
        if not (-90.0 < point_y < 90.0):
            raise ValueError("Place a correct latitude: values between -90.0 and 90.0")
        self._latitude = point_y
    
    @property
    def longitude(self):
        return self._longitude
    
    @longitude.setter
    def longitude(self, point_x):
        try:
            point_x = float(point_x)
        except(ValueError, TypeError):
            raise TypeError("Latitude must be float")
        if not -180.0 < point_x < 180.0:
            raise ValueError("Place a correct longitude: values between -180.0 and 180.0")
        self._longitude = point_x

    def validate(self):
        errors = []
        
        if not self.title:
            errors.append("Title is required")
        
        if not self.description:
            errors.append("Description is required")
        
        if self.price <= 0:
            errors.append("Price must be greater than 0")
        
        if not self.owner_id:
            errors.append("Owner ID is required")
        
        return errors

    
    def add_review(self, review):
        if review not in self.reviews:
            self.reviews.append(review)
    
    def remove_review(self, review):
        if review in self.reviews:
            self.reviews.remove(review)
    
    def add_amenity(self, amenity):
        if amenity not in self.amenities:
            self.amenities.append(amenity)

    def remove_amenity(self, amenity):
        if amenity in self.amenities:
            self.amenities.remove(amenity)
    
    def to_dict(self):
        data = super().to_dict()
        data.update({
            "title": self.title,
            "description": self.description,
            "price": self._price,
            "coordinates": {self._latitude, self._longitude},
            "owner": self.owner_id,
            "amenities": self.amenities,
            "reviews": self.reviews
        })