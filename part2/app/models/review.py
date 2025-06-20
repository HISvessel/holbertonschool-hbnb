"""this is the creation of the file for the review entity:
pending edition, since this is for the structure of our files"""
from base_model import BaseClass

class Review(BaseClass):
    def __init__(self, user_id='', title='',  comment='', rating=0, place_id=''):
        super().__init__()
        self.user_id = user_id
        self.title = title
        self.comment = comment
        self.rating = rating
        self.place_id = place_id

    def to_dict(self):
        data = super().to_dict()
        data.update({
            "comment": self.comment,
            "rating": self.rating,
            "user": self.user_id,
            "place": self.place_id,
        })
        return data
