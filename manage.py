import unittest
from flask.cli import FlaskGroup
from flask import render_template, request, jsonify
from src import app

# app.app_context().push()

cli = FlaskGroup(app)


@app.route("/")
def get_root():
    return render_template("index.html")


@app.route("/api/docs")
def get_docs():
    print("sending docs")
    return render_template("swaggerui.html")


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
