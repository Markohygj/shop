from flask import Flask, render_template, request, flash

app = Flask(__name__)

@app.route("/")
@app.route("/index")
def index():
    return render_template("index.html")

@app.route("/sneekers")
def sneekers():
    return render_template("sneekers.html")

@app.route("/jeans")
def jeaans():
    return render_template("jeans.html")

@app.route("/t-shirt")
def tshirt():
    return render_template("t-shirt.html")

@app.route("/blouse")
def blouse():
    return render_template("blouse.html")

if __name__ == '__main__':
    app.run(debug=True)
