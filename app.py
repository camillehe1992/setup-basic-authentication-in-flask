import unittest
from flask.cli import FlaskGroup
from src import app, utils

app.app_context().push()

cli = FlaskGroup(app)


@cli.command("create_admin")
def create_admin():
    utils.create_admin()


@cli.command("test")
def test():
    """Runs the unit tests."""
    tests = unittest.TestLoader().discover("tests", pattern="test*.py")
    result = unittest.TextTestRunner(verbosity=2).run(tests)
    if result.wasSuccessful():
        return 0
    return 1


if __name__ == "__main__":
    cli()
