

## Diagram

```mermaid 
classDiagram
class User {
  +user_name = string
  +first_name = string
  +last_name = string
  #password = string
  #email = string
  #password = string
  +addUser(User)
  +removeUser(User)
  +submit_review(Review)
  +remove_review(Review)
  +makeAdmin()
  +removeAdmin()
}

class Review {
  +title = string
  +comment = string
  +review_author = User
  +review_rating = int
  +review_date = list[mm,dd,yyyy]
  +submit_review(self)
  +delete_review(self)
}

class Place {
  +place_title = string
  +place_description = string
  +coordinates = []
  +review_rating = int

  +addPlace (Place)
  +removePlace(Place)
  +addAmenity()
  +removeAmenity()
  +totalAmenities()
  +addReview()
}

class Amenity {
  +amenity_name = string
  +amenity_description = string
  +total_amenities = []

  +add_Amenity()
  +list_Amenity()
}

User <--o Review : submits
User o--> Place : searches and books
Place o-- User : adds and manages
Place *..> Amenity : contains
Place o--> Review : subject to
User <..o Amenity : adds and lists