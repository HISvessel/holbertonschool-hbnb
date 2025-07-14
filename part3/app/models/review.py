"""this is the creation of the file for the review entity:
pending edition, since this is for the structure of our files"""
from app.models.base_model import BaseClass
from app.extensions.extensions import db

class Review(BaseClass):
    def __init__(self, user_id='', title='',  comment='', rating=0, place_id=''):
        super().__init__()
        self.user_id = user_id
        self.title = title
        self.comment = comment
        self._rating = rating
        self.place_id = place_id
    
    __tablename__ = 'reviews'
    id = db.Column(db.String, nullable=False)#make a primary key
    title = db.Column(db.String(120), nullable=False)
    comment = db.Column(db.Text, nullable=False)
    rating = db.Column(db.Integer, nullable=False)
    user_id = db.column(db.String(100), nullable=False) #make this a foreign key user.id
    place_id = db.Column(db.String(120), nullable=False) #make this a foreign key referencing place.id

    def validate(self):
        errors = []
        if not self.user_id:
            errors.append("Review must be associated with a user.")
        if not self.place_id:
            errors.append("Review must be associated with a place.")
        if not self.title:
            errors.append("Title is required.")
        if not self.comment:
            errors.append("Comment is required.")
        if not isinstance(self.rating, int) or not (1 <= self.rating <= 5):
            errors.append("Rating must be an integer between 1 and 5.")
        return errors

    @property
    def rating(self):
        return self._rating

    @rating.setter
    def rating(self, input):
        if input < 1:
            raise ValueError("Input must be higher than 0")
        #checking or type checking with isinstance, not TypeError
        if not isinstance(input, int):
            raise TypeError("Input must be an int")
        self._rating = input


    def to_dict(self):
        data = super().to_dict()
        data.update({
            "title": self.title,
            "comment": self.comment,
            "rating": self.rating,
            "user_id": self.user_id,
            "place_id": self.place_id,
        })
        return data
