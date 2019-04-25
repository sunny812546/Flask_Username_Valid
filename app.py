from flask import Flask, render_template, request
app = Flask(__name__)


@app.route("/")
def home():
    return render_template("home.html")


@app.route("/signup", methods=['GET', 'POST'])
def signup():

    if request.method == "POST":
        firstname = request.form["email"]
        number = False
        uppercase = False
        lowwercase = False
        for i in firstname:
            if i.isdigit():
                number = True
            elif i.isupper():
                uppercase = True
            elif i.islower():
                lowwercase = True

        return render_template("thankyou.html", number=number,
                               uppercase=uppercase,
                               lowwecase=lowwercase
                               )
    return render_template("signup.html")


@app.errorhandler(404)
def error(e):
    return render_template("404.html"), 404


if __name__ == "__main__":

    app.run(debug=True, port=5000)
