"""this is the creation of the file for the review entity:
pending edition, since this is for the structure of our files"""
from base_model import BaseClass

class Review(BaseClass):
    def __init__(self, user_id='', text='', rating=0, place_id=''):
        super().__init__()
        self.user_id = user_id
        self.text = text
        self.rating = rating
        self.place_id = place_id

    def add_review_to_place(self, review):
        pass