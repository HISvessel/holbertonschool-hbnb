import sqlite3
from uuid import uuid4
import os
from app.models.user import User

initial_amenities = ['WIFi', 'Swimming Pool', 'Air Conditioning']

ADMIN_ID = "36c9050e-ddd3-4c3b-9731-9f487208bbc1"

def connect_DB():
    db = os.path.abspath(os.path.join(os.path.dirname(__file__), '../part3/app/scripts/hbnb.db'))
    return sqlite3.connect(db)

def insert_admin(cursor):
    admin = User("Admin", "Hbnb", "admin@hbnb.io", "admin1234", is_admin=True)
    admin.id = ADMIN_ID

    cursor.execute("""INSERT INTO users (id, first_name, last_name, email, password, is_admin)
        VALUES (?, ?, ?, ?, ?, ?)""", (admin.id, admin.first_name, admin.last_name, admin.email, admin.password, admin.is_admin))
    
    print("Administrator added successfully")

def insert_amenity(cursor):
    for name in initial_amenities:
        amenity_id = str(uuid4())
        cursor.execute("""INSERT INTO amenities (id, name) VALUES (?, ?)""",
                        (amenity_id, name))
        print(f"Amenity inserted: {name}")

def main():
    conn = connect_DB()
    cursor = conn.cursor()

    insert_admin(cursor)
    insert_amenity(cursor)

    conn.commit()
    conn.close()
    print("Seeding successful!")

if __name__ == "__main__":
    main()
