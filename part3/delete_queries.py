def delete_user(cursor, user_id):
    cursor.execute("DELETE FROM users WHERE id = ?", (user_id,))
    return cursor.rowcount

def delete_place(cursor, place_id):
    cursor.execute("DELETE FROM places WHERE id = ?", (place_id,))
    return cursor.rowcount

def delete_review(cursor, review_id):
    cursor.execute("DELETE FROM reviews WHERE id = ?", (review_id,))
    return cursor.rowcount

def delete_amenity(cursor, amenity_id):
    cursor.execute("DELETE FROM amenities WHERE id = ?", (amenity_id,))
    return cursor.rowcount
