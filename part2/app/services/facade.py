"""the integration of our facade, for interaction and connection between entities"""
from app.persistence.repository import InMemoryRepository
from app.models.user import User

class HbnbFacade():
    def __init__(self):
        self.user_repo = InMemoryRepository()
        self.place_repo = InMemoryRepository()
        self.review_repo = InMemoryRepository()
        self.amenity_repo = InMemoryRepository()
    
    #Placeholder method for creating a user
    def create_user(self, user_data):
        user = User(**user_data)
        errors = user.validate()
        if errors:
            return {"errors": errors}, 400
        self.user_repo.add(user)
        return user
   
    #getting method for obtaining user by id
    def get_user(self, user_id):
        return self.user_repo.get(user_id)
    
    #getting method for user by email
    def get_user_by_email(self, user_email):
        return self.user_repo.get_by_attribute(user_email)


    def get_place(self, place_id):
        pass