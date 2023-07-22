#!/usr/bin/python3
"""
starts a Flask web application:

Your web application must be listening on 0.0.0.0, port 5000
Routes:
/: display “Hello HBNB!”
/hbnb: display “HBNB”
/c/<text>: display “C ” followed by the value of the text
variable (replace underscore _ symbols with a space )

/python/(<text>): display “Python ”, followed by the value of the text
variable (replace underscore _ symbols with a space )
The default value of text is “is cool”
 /number/<n>: Displays 'n is a number' only if <n> is an integer.
/number_template/<n>: Displays an HTML page only if <n> is an integer.

"""


from flask import Flask
from flask import render_template
app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello_hbnb():
    """ display “Hello HBNB!"""
    return ("Hello HBNB!")


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    """Displays 'HBNB'."""
    return "HBNB"


@app.route("/c/<text>", strict_slashes=False)
def c_text(text):
    """Display  “C ” followed by the value of the text variable
    (replace underscore _ symbols with a space ) """
    p_text = text.replace('_', ' ')
    return "C {}".format(p_text)


@app.route("/python", strict_slashes=False)
@app.route("/python/<text>", strict_slashes=False)
def python(text="is cool"):
    """
    display “Python ”, followed by the value of the text variable
    (replace underscore _ symbols with a space )
    The default value of text is “is cool”

    """
    p_text = text.replace('_', ' ')
    return "Python {}".format(p_text)


@app.route("/number/<int:n>", strict_slashes=False)
def is_int_num(n):
    """display “n is a number” only if n is an integer"""
    if isinstance(n, int):
        return "{} is a number".format(n)


@app.route('/number_template/<int:n>', strict_slashes=False)
def number_template(n=None):
    """display a HTML page only if n is an integer"""
    if isinstance(n, int):
        return render_template("5-number.html", n=n)


@app.route('/number_odd_or_even/<int:n>', strict_slashes=False)
def number_odd_or_even(n=None):
    """display a HTML page only if n is an integer:
    H1 tag: “Number: n is even|odd” inside the tag BODY
    """
    if isinstance(n, int):
        if n % 2:
            ev_od = "odd"
        else:
            ev_od = "even"
        return render_template("6-number_odd_or_even.html", n=n, ev_od=ev_od)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=None)
