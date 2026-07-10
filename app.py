from flask import Flask
from database import *

app = Flask(__name__)

app.secret_key = "diamond_secret_key"

create_tables()
create_default_admin()
add_sample_students()
add_sample_candidates()

@app.route("/")
def home():
    return """
    <html>

    <head>

    <title>Digital School Election Booth</title>

    <link href='https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css' rel='stylesheet'>

    </head>

    <body class='bg-light'>

    <div class='container mt-5'>

    <div class='card shadow p-5 text-center'>

    <h1 class='text-success'>
    🗳 Digital School Election Booth
    </h1>

    <h3>
    Diamond English School
    </h3>

    <hr>

    <a class='btn btn-primary btn-lg m-2' href='/student'>
    Student Login
    </a>

    <a class='btn btn-dark btn-lg m-2' href='/admin'>
    Admin Login
    </a>

    </div>

    </div>

    </body>

    </html>
    """

if __name__ == "__main__":
    app.run(debug=True)
