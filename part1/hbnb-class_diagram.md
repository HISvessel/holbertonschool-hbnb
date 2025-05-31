

## Diagram

```mermaid
classDiagram
class User {
  +user_name = string
  +submit_review = string
  +remove_review()
  +addUser
  +removeUser
  +makeAdmin
  +removeAdmin
}

class Place {
  +place_title = string
  +place_description = string
  +lattitude = int
  +longitude = int

  +addPlace (self, place_title, lattitude, longiude)
  +removePlace()
  +addAmenity()
  +removeAmenity()
  +totalAmenities() = []
}

class Review {
  +review = string
  +review_author = string
}

class Amenity {
  +amenity_name = string
  +amenity_description = string
  +total_amenities = []

  add_Amenity()
  list_Amenity()
}

User <|--- Review : gets from
User --> Place : searches for
User --> Review : submits
Place --> Amenity : contains