import unittest
import uuid
from datetime import datetime, UTC

from src import db
from src.model import User
from tests.base import BaseTestCase


class TestUserModel(BaseTestCase):

    def setUp(self):
        self.user = User(
            public_id=str(uuid.uuid4()),
            username="Test User",
            email="test@test.com",
            password="test",
            registered_on=datetime.now(UTC),
        )
        db.session.add(self.user)
        db.session.commit()

        return super().setUp()

    def tearDown(self):
        db.session.delete(self.user)
        db.session.commit()
        return super().tearDown()

    def test_encode_auth_token(self):
        auth_token = self.user.encode_auth_token(self.user.public_id)

        self.assertTrue(isinstance(auth_token, str))

    def test_decode_auth_token(self):
        auth_token = self.user.encode_auth_token(self.user.public_id)
        public_id = User.decode_auth_token(auth_token)

        self.assertTrue(isinstance(auth_token, str))
        self.assertTrue(public_id == self.user.public_id)


if __name__ == "__main__":
    unittest.main()
