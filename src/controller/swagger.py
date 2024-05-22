from flask import Blueprint, render_template, current_app as app

swagger_bp = Blueprint("swagger", __name__)


@swagger_bp.route("/")
def get_root():
    return render_template("index.html")


@swagger_bp.route("/api/docs")
def get_docs():
    print("sending docs")
    return render_template("swaggerui.html")
