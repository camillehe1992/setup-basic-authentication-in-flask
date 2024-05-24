from sqlalchemy_serializer import SerializerMixin
from datetime import datetime, timedelta, UTC
import jwt

from src import db, bcrypt
from src.config import key
from src.model.blacklist import BlacklistToken


class User(db.Model, SerializerMixin):
    """User Model for storing user related details"""

    serialize_only = ("public_id", "email", "username", "is_admin", "is_confirmed")
    serialize_rules = ()

    __tablename__ = "user"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    public_id = db.Column(db.String(100), unique=True)
    email = db.Column(db.String(255), unique=True, nullable=False)
    username = db.Column(db.String(50), unique=False, nullable=False)
    password_hash = db.Column(db.String(100))
    is_admin = db.Column(db.Boolean, nullable=False, default=False)
    is_confirmed = db.Column(db.Boolean, nullable=False, default=False)
    registered_on = db.Column(db.DateTime, nullable=False)

    @property
    def password(self):
        raise AttributeError("password: write-only field")

    @password.setter
    def password(self, password):
        self.password_hash = bcrypt.generate_password_hash(password).decode("utf-8")

    def check_password(self, password):
        return bcrypt.check_password_hash(self.password_hash, password)

    def encode_auth_token(self, public_id):
        """
        Generates the Auth Token
        :return: string
        """
        try:
            payload = {
                "exp": datetime.now(UTC) + timedelta(days=1, seconds=5),
                "iat": datetime.now(UTC),
                "sub": public_id,
            }
            return jwt.encode(payload, key, algorithm="HS256")
        except Exception as e:
            return e

    @staticmethod
    def decode_auth_token(auth_token):
        """
        Decodes the auth token
        :param auth_token:
        :return: integer|string
        """
        try:
            payload = jwt.decode(auth_token, key, algorithms=["HS256"])
            is_blacklisted_token = BlacklistToken.check_blacklist(auth_token)
            if is_blacklisted_token:
                return "Token blacklisted. Please log in again."
            else:
                return payload["sub"]
        except jwt.ExpiredSignatureError:
            return "Signature expired. Please log in again."
        except jwt.InvalidTokenError:
            return "Invalid token. Please log in again."

    def __repr__(self):
        return "<User '{}'>".format(self.email)
