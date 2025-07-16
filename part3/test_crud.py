import sqlite3
from uuid import uuid4
from app.models.amenity import Amenity
from app.models.places import Place
from app.models.review import Review
from app.models.user import User
from create_queries import *
from read_queries import *
from update_queries import *
from delete_queries import *

DB_PATH = "../part3/app/scripts/hbnb.db"

def run_test():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

def run_tests():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    # 🧪 1. CREATE
    print("\n[CREATE]")
    user = User("Test", "User", "test@user.com", "securepass")
    user.id = str(uuid4())
    user.is_admin = False

    place = Place()
    place.id = str(uuid4())
    place.title = "Test Place"
    place.description = "Test Description"
    place.price = 99.99
    place.latitude = 18.4
    place.longitude = -66.1
    place.owner_id = user.id

    amenity = Amenity()
    amenity.id = str(uuid4())
    amenity.name = "Test Amenity"

    review = Review(str(uuid4()),'Nice Stay', 'It was a great time', 4)
    #review.id = str(uuid4())
    #review.title = "Nice stay"
    #review.comment = "It was a great time"
    #review.rating = 4
    review.user_id = user.id
    review.place_id = place.id

    create_user(cursor, user)
    create_place(cursor, place)
    create_amenity(cursor, amenity)
    create_review(cursor, review)

    conn.commit()

    # 🧪 2. READ
    print("\n[READ]")
    print("User:", get_user_by_email(cursor, user.email))
    print("Place:", get_place_by_id(cursor, place.id))
    print("Amenity:", get_amenity_by_name(cursor, amenity.name))
    print("Review by user:", get_review_by_user(cursor, user.id))

    # 🧪 3. UPDATE
    print("\n[UPDATE]")
    update_user_name(cursor, user.id, "Updated", "Name")
    update_place_description(cursor, place.id, "Updated description")
    update_review_comment(cursor, review.id, "Updated comment")
    update_amenity_name(cursor, amenity.id, "Updated Amenity")
    conn.commit()

    print("Updated User:", get_user_by_email(cursor, user.email))
    print("Updated Place:", get_place_by_id(cursor, place.id))
    print("Updated Review:", get_review_by_user(cursor, user.id))
    print("Updated Amenity:", get_amenity_by_name(cursor, "Updated Amenity"))

    # 🧪 4. DELETE
    print("\n[DELETE]")
    delete_review(cursor, review.id)
    delete_place(cursor, place.id)
    delete_user(cursor, user.id)
    delete_amenity(cursor, amenity.id)
    conn.commit()

    print("Review after delete:", get_review_by_user(cursor, user.id))
    print("Place after delete:", get_place_by_id(cursor, place.id))
    print("User after delete:", get_user_by_email(cursor, user.email))
    print("Amenity after delete:", get_amenity_by_name(cursor, "Updated Amenity"))

    conn.close()
    print("\n[✔️ TEST COMPLETE]")

if __name__ == "__main__":
    run_tests()
