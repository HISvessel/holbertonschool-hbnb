"""this is the file for the creation of our place entity; changes pending
as this is for file structure"""
from app.models.base_model import BaseClass
from app.extensions.extensions import db
from sqlalchemy.orm import validates


class Place(BaseClass):
    def __init__(self, title='', description='', owner_id='',
                 latitude=0.0, longitude=0.0, price=0.0, amenities=None, reviews=None):
        super().__init__()
        self.title = title
        self.description = description
        self.price = price # not underscore
        self.latitude = latitude
        self.longitude = longitude
        self.owner_id = owner_id
        self.amenities = amenities if amenities is not None else []
        self.reviews = reviews if reviews is not None else []

        #self.price = price
        #self.latitude = latitude
        #self.longitude = longitude
    
    __tablename__ = 'places'
    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=False)
    price = db.Column(db.Float, nullable=False)
    latitude = db.Column(db.Float, nullable=False)
    longitude = db.Column(db.Float, nullable=False)
    owner_id = db.Column(db.String, db.ForeignKey("users.id"), nullable=False) # will make a foreign key referencing user.id
    
    @validates('price')
    def validate_price(self, key, value):
        try:
           value = float(value)
        except (ValueError, TypeError):
            raise TypeError("Price must be a float")
        if value < 0:
            raise ValueError("Price cannot be negative")
        return value

    @validates('latitude')
    def validate_latitude(self, key, value):
        try:
            value = float(value)
        except(ValueError, TypeError):
            raise TypeError("Latitude must be float")
        if not (-90.0 <= value <= 90.0):
            raise ValueError("Place a correct latitude: values between -90.0 and 90.0")
        return value

    @validates('longitude')
    def validate_longitude(self, key, value):
        try:
            value = float(value)
        except(ValueError, TypeError):
            raise TypeError("Longitude must be float")
        if not (-180.0 <= value <= 180.0):
            raise ValueError("Place a correct longitude: values between -180.0 and 180.0")
        return value

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
            "price": self.price,
            #"coordinates": {self._latitude, self._longitude},
            "latitude": self.latitude,
            "longitude": self.longitude,
            "owner": self.owner_id,
            #"amenities": self.amenities,
            #"reviews": self.reviews
        })
        return data