"""the integration of our facade, for interaction and connection between entities"""
from app.persistence.repository import InMemoryRepository
from app.models.user import User
from app.models.amenity import Amenity
from app.models.places import Place
from app.models.review import Review

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
    

    """Part2 of our facade: implementing the facade between
    the Place APIs and the Place class"""

    def create_place(self, place_data):
        place = Place(**place_data)
        errors = place.validate()
        if errors:
            return {"errors": errors}, 400
        self.place_repo.add(place)
        return place

    def get_place(self, place_id):
        return self.place_repo.get(place_id)

    def get_all_places(self):
        places = self.place_repo.get_all()
        return places

    #def get_places_by_review(self, value):
        """a facade function that allows us to search by filtering
        all reviews of the same 0 to 5 star rating, which is tied to the
        place's overall review meter and not by the review entity itself"""
    #    pass

    #def get_places_by_amenity(self, data_id):
        """This is a potential model that searches
        all existing place by filtering the contents of 
        the list of all existing places and finding the amenity
        name in the amenity dictionary's name key"""
    #    pass

    def update_place(self, place_id, updated_data):
        place = self.place_repo.get(place_id)
        if not place:
            return None
        place.update(updated_data)
        return place

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
        return self.amenity_repo.get_all()

    def update_amenity(self, amenity_id, updated_data):
        amenity = self.amenity_repo.get(amenity_id)
        if not amenity:
            return None
        amenity.update(updated_data)
        return amenity

    """part 4: models for CRUDding reviews"""

    def create_review(self, review_data):
        review = Review(**review_data)
        errors = review.validate()
        if errors:
            return {"errors": errors}, 404
        self.review_repo.add(review)
        return review

    def get_review(self, review_id):
        return self.review_repo.get(review_id)

    def get_all_reviews(self):
        return self.review_repo.get_all()
    
    def update_review(self, review_id, updated_data):
        review = self.review_repo.get(review_id)
        if not review:
            return None
        review.update(updated_data)
        return review
    
    def delete_review(self, review_id):
        review = self.review_repo.get(review_id)
        if review:
            review.delete(review_id)