--the following scripts are for the creation of our database schema--
--we will create tables one by one--

CREATE TABLE IF NOT EXISTS users (
    id VARCHAR (60) PRIMARY KEY,
    first_name VARCHAR(255) NOT NULL,
    last_name VARCHAR(255) NOT NULL,
    email VARCHAR(255) UNIQUE NOT NULL, 
    password VARCHAR(255) NOT NULL,
    is_admin BOOLEAN DEFAULT FALSE
);

CREATE TABLE IF NOT EXISTS places (
    id VARCHAR (60) PRIMARY KEY,
    title VARCHAR(255) NOT NULL,
    description TEXT,
    price DECIMAL(10, 2), 
    password VARCHAR(255) NOT NULL,
    latitude FLOAT,
    longitude FLOAT,
    owner_id VARCHAR(36),
    FOREIGN KEY (owner_id) REFERENCES user(id)
);

CREATE TABLE IF NOT EXISTS reviews (
    id VARCHAR (60) PRIMARY KEY,
    title VARCHAR(255) NOT NULL,
    comment VARCHAR(255) NOT NULL,
    rating INT CHECK (rating BETWEEN 1 AND 5),
    user_id VARCHAR(255), 
    place_id VARCHAR(255),
    FOREIGN KEY (user_id) REFERENCES user(id),
    FOREIGN KEY (place_id) REFERENCES places(id),
    UNIQUE(user_id, place_id)
);

CREATE TABLE IF NOT EXISTS amenities (
    id VARCHAR (60) PRIMARY KEY,
    name VARCHAR(255) UNIQUE NOT NULL
);

CREATE TABLE IF NOT EXISTS places_amenities (
    place_id VARCHAR(60),
    amenity_id VARCHAR(60),
    PRIMARY KEY (place_id, amenity_id),
    FOREIGN KEY (amenity_id) REFERENCES amenities(id),
    FOREIGN KEY (place_id) REFERENCES places(id)
);