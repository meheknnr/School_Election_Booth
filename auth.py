from flask import Blueprint, render_template, request, redirect, session, flash
from database import get_connection

auth = Blueprint("auth", __name__)

# -------------------------
# Student Login
# -------------------------
@auth.route("/student", methods=["GET", "POST"])
def student_login():

    if request.method == "POST":

        student_id = request.form["student_id"]
        password = request.form["password"]

        conn = get_connection()

        student = conn.execute(
            "SELECT * FROM students WHERE student_id=? AND password=?",
            (student_id, password)
        ).fetchone()

        conn.close()

        if student:

            session["student"] = student["student_id"]

            return redirect("/vote")

        flash("Invalid Student ID or Password")

    return render_template("student_login.html")


# -------------------------
# Logout
# -------------------------
@auth.route("/logout")
def logout():

    session.clear()

    return redirect("/")
