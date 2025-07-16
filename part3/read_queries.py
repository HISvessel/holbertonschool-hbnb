
def get_user_by_email(cursor, email):
    cursor.execute("SELECT * FROM users WHERE email = ?", (email,))
    return cursor.fetchone()

def get_all_user(cursor):
    cursor.execute("SELECT * FROM users")
    return cursor.fetchall()

def get_place_by_id(cursor, place_id):
    cursor.execute("SELECT * FROM places where id = ?", (place_id,))
    return cursor.fetchone()

def get_all_places(cursor):
    cursor.execute("SELECT * FROM places")
    return cursor.fetchall()

def get_review_by_user(cursor, user_id):
    cursor.execute("SELECT * FROM reviews WHERE user_id = ?", (user_id,))
    return cursor.fetchall()

def get_reviews_for_place(cursor, place_id):
    cursor.execute("SELECT * FROM reviews WHERE place_id = ?", (place_id,))
    return cursor.fetchall()

def get_all_reviews(cursor):
    cursor.execute("SELECT * FROM reviews")
    return cursor.fetchall()

def get_amenity_by_name(cursor, name):
    cursor.execute("SELECT * FROM amenities WHERE name = ?", (name,))
    return cursor.fetchone()

def get_all_amenities(cursor):
    cursor.execute("SELECT * FROM amenities")
    return cursor.fetchall()
