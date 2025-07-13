"""this begins the creation of our user entity; changes pending, as this is for structure"""
from app.models.base_model import BaseClass
import bcrypt
import re
from app.extensions.extensions import db


class User(BaseClass):

    """Represents a user in our system."""
    
    def __init__(self, first_name="", last_name="", email="", password="", is_admin=0):

        """Initialize a new user."""
        super().__init__()  # Call parent class constructor
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.places = []
        self._is_admin = False  # Regular user by default
 

        # Hash the password for security
    
        self.password_hash = self._hash_password(password) if password else None
    
    __tablename__ = 'users' #or instead here
    first_name = db.Column(db.String(50), nullable=False)
    last_name = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(120), nullable=False, unique=True)
    password = db.Column(db.String(120), nullable=False)
    is_admin = db.Column(db.Boolean, default=False)

    def _hash_password(self, password):
        """Hash a password for storing."""
        # Convert password to bytes and hash it
        salt = bcrypt.gensalt()
        return bcrypt.hashpw(password.encode('utf-8'), salt).decode('utf-8')
    
    def verify_password(self, password):
        if not self.password_hash:
            return False
        return bcrypt.checkpw(
            password.encode('utf-8'), 
            self.password_hash.encode('utf-8') # remove the variable, simply result later
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
        if not self.password_hash:
            errors.append("Password is required")
        
        return errors
    
    def _is_valid_email(self, email):
        """Check if email format is valid."""
        pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
        return re.match(pattern, email) is not None
    
    def set_admin_status(self, status):
        #set admin status using True/False
        if not isinstance(status, int):
            raise TypeError("Status must be an int(0 or 1)")
        if status not in (0, 1):
            raise ValueError("Admin status must be 0 or 1")
        self._is_admin = bool(status)

    @property #this might now be unreliable with database integration
    def is_admin(self):
        return self._is_admin
    
    def promote_to_admin(self):
        self._is_admin = True
    
    def demote_from_admin(self):
        self._is_admin = False

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