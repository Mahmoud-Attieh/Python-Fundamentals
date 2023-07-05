from flask import Flask , render_template, session

app = Flask(__name__)
app.secret_key = "my_secret_key"
counter = 1
@app.route("/")
def main():
    if 'counter' not in session:
        session['counter']=0
    session['counter'] += 1 
    return render_template('index.html', counter = session['counter'])

@app.route("/destroy")
def destroy():
    session['counter'] = 0
    return render_template('index.html')

if __name__=="__main__":
    app.run(debug=True)    