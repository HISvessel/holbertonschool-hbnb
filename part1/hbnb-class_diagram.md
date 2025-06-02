

## Diagram

```mermaid
classDiagram
class User {
  +user_name = string
  +submit_review()
  +remove_review()
  +addUser
  +removeUser
  +makeAdmin
  +removeAdmin
}

class Place {
  +place_title = string
  +place_description = string
  +coordinates = []
  +review_rating = int

  +addPlace (self, place_title, coordinates)
  +removePlace()
  +addAmenity()
  +removeAmenity()
  +totalAmenities() []
  addReview()
}

class Review {
  +review = string
  +review_author = string
  +review_rating = int
  +review_date = []
  submit_review()
  delete_review()
}

class Amenity {
  +amenity_name = string
  +amenity_description = string
  +total_amenities = []

  add_Amenity()
  list_Amenity()
}

User <-- Review : submitted by
User o--> Place : searches and reserves
User --o Review : submits
Place *..> Amenity : contains
Place o--> Review : subject to