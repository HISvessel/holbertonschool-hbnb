def update_user_email(cursor, user_id, email):
    cursor.execute("UPDATE users SET email = ? WHERE id = ?", (email, user_id))
    return cursor.rowcount

def update_user_password(cursor, user_id, password):
    cursor.execute("UPDATE users SET password = ? WHERE id = ?", (password, user_id))
    return cursor.rowcount

def update_user_name(cursor, user_id, first_name, last_name):
    cursor.execute("UPDATE users SET first_name = ?, last_name = ? WHERE id = ?", (first_name, last_name, user_id))
    return cursor.rowcount

def update_place_price(cursor, price, place_id):
    cursor.execute("UPDATE places SET price = ? WHERE id = ?", (price, place_id))
    return cursor.rowcount

def update_place_description(cursor, description, place_id):
    cursor.execute("UPDATE places SET description = ? WHERE id = ?", (description, place_id))
    return cursor.rowcount

def update_review_rating(cursor, review_id, rating):
    cursor.execute("UPDATE reviews SET rating = ? WHERE id = ?", (rating, review_id))
    return cursor.rowcount

def update_review_comment(cursor, review_id, comment):
    cursor.execute("UPDATE reviews SET comment = ? WHERE id = ?", (comment, review_id))
    return cursor.rowcount

def update_amenity_name(cursor, amenity_id, name):
    cursor.execute("UPDATE amenities SET name = ? WHERE id = ?", (name, amenity_id))
    return cursor.rowcount