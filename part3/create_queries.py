

def create_amenity(cursor, amenity):
    """creates simple amenity with a name and an id"""
    cursor.execute("""INSERT OR IGNORE INTO amenities (id, name) VALUES (?, ?)""", 
                   (amenity.id, amenity.name))

def create_place(cursor, place):
    """creates a place if not exists
    avoids duplicates with UNIQUE PK constraints"""
    cursor.execute("""INSERT OR IGNORE INTO places 
                   (id, title, description, price, latitude, longitude, owner_id) 
                   VALUES (?, ?, ?, ?, ?, ?, ?)""", 
                   (place.id,
                    place.title,
                    place.description,
                    place.price,
                    place.latitude,
                    place.longitude,
                    place.owner_id
                    ))
    
def create_review(cursor, review):
    """creates a review if not exists
    avoids duplicates with UNIQUE and PK constraints"""
    cursor.execute("""INSERT OR IGNORE INTO reviews 
                   (id, title, comment, rating, user_id, place_id)
                   VALUES (?, ?, ?, ?, ?, ?)""", 
                   (review.id,
                    review.title,
                    review.comment,
                    review.rating,
                    review.user_id,
                    review.place_id))

def create_user(cursor, user):
    """creates a review if not exists, else ignore
    avoids duplicates by email with UNIQUE and PK constraints"""
    cursor.execute("""INSERT OR IGNORE INTO users 
                   (id, first_name, last_name, email, password, is_admin)
                   VALUES (?, ?, ?, ?, ?, ?)""",
                   (user.id,
                    user.first_name,
                    user.last_name,
                    user.email,
                    user.password,
                    user.is_admin))
