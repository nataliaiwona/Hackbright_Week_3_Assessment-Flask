from flask import Flask, render_template, request, redirect
from flask_debugtoolbar import DebugToolbarExtension


app = Flask(__name__)


# Required to use Flask sessions and the debug toolbar
app.secret_key = "ABC"

@app.route("/")
def index_page():
    """Show an index page."""

    # return "<html><body>This is the homepage.</body></html>"

    # Alternately, we could make this a Jinja template in `templates/`
    # and return that result of rendering this, like:
    #
    return render_template("index.html")

@app.route("/application-form")
def show_application():
    """Show application form."""

    return render_template("application-form.html")

@app.route("/application-response", methods=["POST"])
def give_response():
    """Returns response that acknowledges application."""

    firstname = request.form.get("firstname")
    lastname = request.form.get("lastname")
    openpositions = request.form.get("openpositions")
    salaryrequirement = request.form.get("salaryrequirement")

    return render_template("application-response.html",
                            firstname=firstname,
                            lastname=lastname,
                            openpositions=openpositions,
                            salaryrequirement=salaryrequirement)

if __name__ == "__main__":
    # We have to set debug=True here, since it has to be True at the
    # point that we invoke the DebugToolbarExtension
    app.debug = True

    # Use the DebugToolbar
    DebugToolbarExtension(app)

    app.run(host="0.0.0.0")






















