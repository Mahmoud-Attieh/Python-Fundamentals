from flask import Flask ,render_template

app = Flask(__name__)

@app.route("/play")
def hello_world():
    return render_template("index.html")

@app.route("/play/<x>")
def boxNumber(x):
    return render_template("index2.html",x=int(x))

@app.route("/play/<x>/<color>")
def boxColor(x,color):
    return render_template("index3.html",x=int(x) ,color=color)
if __name__ == ("__main__"):
    app.run(debug=True)
