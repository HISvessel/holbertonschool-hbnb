
## Diagram

```mermaid
erDiagram
USER {
    string id PK
    string first_name
    string last_name
    string email
    string password
    boolean is_admin
    timestamp created_at
    timestamp updated_at
}
PLACE {
    string id PK
    string title
    string description
    float price
    float latitude
    float longitude
    string owner_id FK
    timestamp created_at
    timestamp updated_at
}
REVIEW {
    string id PK
    string title
    string comment
    int rating
    string user_id FK
    string place_id FK
    timestamp created_at
    timestamp updated_at
}
AMENITY {
    string id PK
    string name
}
PLACE_AMENITY{
    string place_id FK
    string amenity_id FK
}
USER ||--|{ PLACE : "owns"
USER ||--|{ REVIEW : "creates"
PLACE ||--|{ REVIEW : "is appraised with"
PLACE |{--|{ PLACE_AMENITY : "can feature"
AMENITY |{--|{ PLACE_AMENITY : "is assigned to"
