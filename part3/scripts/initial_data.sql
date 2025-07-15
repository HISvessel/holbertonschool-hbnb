--this script creates initial data for storing an administrator and
--some initial amenities that can be stored as retrievable objects for 
-- existing places

--inserting an administrator user
INSERT INTO users (id, first_name, last_name, email, password, is_admin) VALUES(
'36c9050e-ddd3-4c3b-9731-9f487208bbc1',
'Admin',
'Hbnb',
'admin@hbnb.io'
'$2b$12$D1ynRT8fDn2jkDwM1asGEOv/4kW7cO29tchcN2cUyXnKFDLLuv27m'
TRUE
);

--inserting some initial amenities
INSERT INTO amenities (id, name) VALUES
    ('d7f3c18e-1d4a-4a8d-a877-2c1a5d77e9aa', 'Wifi'),
    ('dc8c5a61-46ea-42d4-9e2f-7b25f1a6d981', 'Swimming Pool'),
    ('dd3a4233-6a7a-4052-9f35-7eddbde63122', 'Air Conditioner');
