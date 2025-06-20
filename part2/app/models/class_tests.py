"""this file is for testing the classes as they are so far.
Our first test is to create a User before implementing on our API"""

from user import User
from places import Place
from review import Review
from amenity import Amenity

def test_user_creation():
    user = User(first_name="Joseph", last_name="Gleason", email="joe.g@example.com")
    assert user.first_name == "Joseph"
    assert user.last_name == "Gleason"
    assert user.email == "joe.g@example.com"
    assert user.is_admin == False
    print("User creation test passed")

def test_place_creation():
    owner = User(first_name="Kevin", last_name="Sanchez", email="kevin.s@example.com")
    place = Place(title="New place", description="A roomy brand new place", owner_id=owner, latitude=32.02, longitude=98.0, price=125.0)
    review = Review(title='Lovely stay', comment='This was a good stay', rating=4, place_id=place, user_id=owner)
    
    owner.add_place(place)
    print("Place successfully added and user-place relationship confirmed!")
    place.add_review(review)
    print("Review submission success!")

    assert place.title == "New place"
    assert place.description == "A roomy brand new place"
    assert place.price == 125.0
    assert len(place.reviews) == 1
    assert place.reviews[0].rating == 4
    assert place.reviews[0].comment == "This was a good stay"
    amenity = test_amenity_creation
    place.add_amenity(amenity)
    print("Place creation and place-review/place-relationship relationship success")

def test_amenity_creation():
    amenity = Amenity(amenity_name="Wifi")
    assert amenity.amenity_name == "Wifi"
    print("Amenity successfully added!")

test_user_creation()
test_place_creation()
