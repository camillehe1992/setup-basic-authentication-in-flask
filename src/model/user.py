from .. import db, bcrypt


class User(db.Model):
    """User Model for storing user related details"""

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

    def __repr__(self):
        return "<User '{}'>".format(self.email)
