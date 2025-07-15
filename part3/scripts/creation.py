#!/usr/bin/python3

from app.extensions.extensions import db
from app.models.user import User
from app.models.places import Place
from app.models.review import Review
from app.models.amenity import Amenity


"""this module is for the creation of a table if it does not exist.
If a table exists, it should not fail upon creation."""


def get_user_by_id(user_id):
    return User.query.filter_by(id=user_id).first()


def get_places_by_user(user_id):
    """this function is defined to retrieve places owned by a user"""

    #this retrieves the user id given as a parameter
    user = get_user_by_id(user_id)

    #returns an empty list if no valid user and its places exist
    if not user:
        return []
    return user.places


if __name__ == "__main__":

    #this retrieves the user from the database
    raw_id = User.query.get(User.id)
    user_id = get_user_by_id(raw_id)

    #this retrieve the places owned by the user given its id
    places = get_places_by_user(user_id)

    #we iterate through all the owned places and print them one by one
    for place in places:
        print(f'{place.title} - {place.description} - {place.price}')
