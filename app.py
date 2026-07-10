from flask import Flask, render_template

from database import *

from auth import auth

app = Flask(__name__)

app.secret_key = "diamond_secret_key"

create_tables()
create_default_admin()
add_sample_students()
add_sample_candidates()

app.register_blueprint(auth)

@app.route("/")
def home():

    return render_template("home.html")

if __name__ == "__main__":
    app.run(debug=True)
