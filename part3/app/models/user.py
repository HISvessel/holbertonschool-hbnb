"""this begins the creation of our user entity; changes pending, as this is for structure"""
from app.models.base_model import BaseClass
import bcrypt
import re
from app.extensions.extensions import db
from sqlalchemy.orm import validates, relationship


class User(BaseClass):

    """Represents a user in our system."""
    
    def __init__(self, first_name="", last_name="", email="", password="", is_admin=0):

        """Initialize a new user."""
        super().__init__()  # Call parent class constructor
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.places = []
        self.is_admin = bool(is_admin) # Regular user by default
 

        # Hash the password for security
        #removed the hash segment from variable
        self.password = self._hash_password(password) if password else None
    
    __tablename__ = 'users' #or instead here
    #id = db.Column(db.String(60), primary_key=True)
    first_name = db.Column(db.String(50), nullable=False)
    last_name = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(120), nullable=False, unique=True)
    password= db.Column(db.String(120), nullable=False, unique=True)
    is_admin = db.Column(db.Boolean, default=False)

    places = relationship('Place', backref='owner', lazy=True, cascade='all, delete_orphan')
    review = relationship('Review', backref='user', lazy=True, cascade='all, delete_orphan')

    def _hash_password(self, password):
        """Hash a password for storing."""
        # Convert password to bytes and hash it
        salt = bcrypt.gensalt()
        return bcrypt.hashpw(password.encode('utf-8'), salt).decode('utf-8')
    
    def verify_password(self, password):
        if not self.password: #removed the has segment from variable
            return False
        return bcrypt.checkpw(
            password.encode('utf-8'), 
            self.password.encode('utf-8') # removed the hash segment from variable
        )

    def validate(self):
        """Check if user data is valid."""
        errors = []
        
        # Check first name
        if not self.first_name or len(self.first_name.strip()) == 0:
            errors.append("First name is required")
        
        # Check last name
        if not self.last_name or len(self.last_name.strip()) == 0:
            errors.append("Last name is required")
        
        # Check email
        if not self.email:
            errors.append("Email is required")
        elif not self._is_valid_email(self.email):
            errors.append("Invalid email format")
        
        # Check password
        if not self.password: #removed hash keyword from variable name
            errors.append("Password is required")
        
        return errors
    
    def _is_valid_email(self, email):
        """Check if email format is valid."""
        pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
        return re.match(pattern, email) is not None


    def promote_to_admin(self):
        self.is_admin = True
    
    def demote_from_admin(self):
        self.is_admin = False

    def add_place(self, place):
        if self.is_admin == True and place not in self.places:
            self.places.append(place)

    def to_dict(self):
        """Convert to dictionary, excluding password."""
        data = super().to_dict()
        data.update({
            'first_name': self.first_name,
            'last_name': self.last_name,
            'email': self.email,
            'is_admin': self.is_admin
        })
        # Never include password in response!
        return data