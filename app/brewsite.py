from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/breweries")
def breweries():
    return render_template("breweries.html")

@app.route("/beer_types")
def beer_types():
    return render_template("beer_types.html")

@app.route("/about")
def about():
    return render_template("about.html")

if __name__ == "__main__":
    app.run(debug=True)
