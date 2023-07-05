from flask import Flask, render_template
app=Flask(__name__)

@app.route('/')
def checkboard():
    num=8
    return render_template("index1.html",num = num)

@app.route('/<num>')
def checkboard_1(num=4):
    num=int(num)
    return render_template("index1.html",num = num )

@app.route("/<x>/<y>")
def checkboard_2(x,y):
    input_1 = int(x)
    input_2 = int(y)
    return render_template("index2.html", input_1=input_1 , input_2 = input_2)

if __name__=="__main__":
    app.run(debug=True)
