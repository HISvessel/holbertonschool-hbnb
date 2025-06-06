

## Diagram

```mermaid 
classDiagram
class User {
  -String first_name
  -String last_name
  -String email
  -String password
  -Boolean is_Admin
  -DateTime created_at
  -DateTime updated_at
  +register() void
  +update_profile() void
  +delete() void
}

class Place {
 -String id
 -String title
 -String description
 -Float price
 -Float longitude
 -Float latitude
 -DateTime created_at
 -DateTime updated_at
 +create() void
 +update() void
 +delete() void
 +add_amenity() void
 +remove_amenity() void
}

class Review {
  -String id
  -Integer rating
  -String comment
  -DateTime created_at
  -DateTime updated_at
  +create() void
  +update() void
  +delete() void
}

class Amenity {
  -String id
  -String name
  -string description
  -DateTime created_at
  -DateTime updated_at
  +create() void
  +update() void
  +delete() void
}

User <--o Review : submits
User o--> Place : searches and books
Place o-- User : owns
Place *..> Amenity : includes
Place o--> Review : has