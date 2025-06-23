"""the integration of our facade, for interaction and connection between entities"""
from app.persistence.repository import InMemoryRepository
from app.models.user import User
from app.models.amenity import Amenity

class HbnbFacade():
    def __init__(self):
        self.user_repo = InMemoryRepository()
        self.place_repo = InMemoryRepository()
        self.review_repo = InMemoryRepository()
        self.amenity_repo = InMemoryRepository()
    
    """Part 1 of our facade: implementing the facade between
    the User API and the User class"""
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
    def get_user_by_email(self, email):
        return self.user_repo.get_by_attribute("email", email)
    
    def get_all_users(self):
        return self.user_repo.get_all()
    
    def update_user(self, user_id, updated_data):
        user = self.user_repo.get(user_id)
        if not user:
            return None
        user.update(updated_data)
        return user
    
    #def delete_user(self, user_id):
        #del self.user_repo(user_id)

    """Part2 of our facade: implementing the facade between
    the Place APIs and the Place class"""

    def get_place(self, place_id):
        pass

    """Part 3 of our facade: implementing the facade between
    the Amenity API and the Amenity class"""

    def create_amenity(self, amenity_data):
        amenity = Amenity(**amenity_data)
        errors = amenity.validate()
        if errors:
            return {"error": errors}, 400
        self.amenity_repo.add(amenity)
        return amenity

    def get_amenity(self, amenity_id):
        return self.amenity_repo.get(amenity_id)

    def get_all_amenities(self):
        pass

    def update_amenities(self, amenity_id, amenity_data):
        pass