from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/")
def index_page():
    """Show an index page."""

    # return "<html><body>This is the homepage.</body></html>"

    # Alternately, we could make this a Jinja template in `templates/`
    # and return that result of rendering this, like:
    #
    return render_template("index.html")



@app.route("/application-form")
def application_form():
    """application-form."""

    return render_template("application-form.html")


@app.route("/application-response", methods=['POST'])
def application_response():
    """application-response."""
    first_name = request.form.get("fname")
    last_name = request.form.get("lname")
    salary = request.form.get("salary")
    job = request.form.get("job")


    return render_template("application-response.html", first_name=first_name,last_name=last_name, salary=salary,job=job)


if __name__ == "__main__":
    app.run(debug=True)
