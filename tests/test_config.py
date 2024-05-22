import unittest
from flask_testing import TestCase
from flask import current_app

from app import app


class TestDevelopmentConfig(TestCase):
    def create_app(self):
        app.config.from_object("src.config.DevelopmentConfig")
        return app

    def test_app_is_development(self):
        self.assertTrue(app.config["ENVIRONMENT"] == "dev")
        self.assertFalse(app.config["SECRET_KEY"] == "palceholder")
        self.assertTrue(app.config["DEBUG"] is True)
        self.assertFalse(current_app is None)
        self.assertFalse(app.config["SQLALCHEMY_DATABASE_URI"] == "palceholder")


class TestTestingConfig(TestCase):
    def create_app(self):
        app.config.from_object("src.config.TestingConfig")
        return app

    def test_app_is_testing(self):
        self.assertTrue(app.config["ENVIRONMENT"] == "test")
        self.assertFalse(app.config["SECRET_KEY"] == "palceholder")
        self.assertTrue(app.config["DEBUG"])
        self.assertFalse(app.config["SQLALCHEMY_DATABASE_URI"] == "palceholder")


class TestProductionConfig(TestCase):
    def create_app(self):
        app.config.from_object("src.config.ProductionConfig")
        return app

    def test_app_is_production(self):
        self.assertTrue(app.config["ENVIRONMENT"] == "prod")
        self.assertFalse(app.config["SECRET_KEY"] == "palceholder")
        self.assertTrue(app.config["DEBUG"] is False)
        self.assertFalse(app.config["SQLALCHEMY_DATABASE_URI"] == "palceholder")


if __name__ == "__main__":
    unittest.main()
