"""the integration of our facade, for interaction and connection between entities"""
from app.persistence.repository import InMemoryRepository


class HbnbFacade():
    def __init__(self):
        self.user_repo = InMemoryRepository()
        self.place_repo = InMemoryRepository()
        self.review_repo = InMemoryRepository()
        self.amenity_repo = InMemoryRepository()
    
    #Placeholder method for creating a user
    def create_user(self, user_data):
        pass

    def get_place(seld, place_id):
        pass