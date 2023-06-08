from flask import Blueprint, render_template, request, flash

views = Blueprint("views", __name__)


@views.route("/")
def home():
    return render_template("home.html")


@views.route("/login", methods=["GET", "POST"])
def login():
    return render_template("login.html")


@views.route("/signup", methods=["GET", "POST"])
def logout():
    if request.method == "POST":
        email = request.form.get("email")
        firstName = request.form.get("firstName")
        password1 = request.form.get("password1")
        password2 = request.form.get("password2")

        if len(password1) < 8:
            flash("password must be atleast 8 characters", category="error")
        elif password1 != password2:
            flash("password don't match", category="error")
        else:
            flash("New account Created", category="success")
    return render_template("signup.html")
