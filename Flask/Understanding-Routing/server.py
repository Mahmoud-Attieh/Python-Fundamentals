from flask import Flask
app = Flask(__name__)
@app.route('/') 
def hello_world():
    return 'Hello World!'

@app.route('/dojo') 
def dojo():
    return 'Dojo!'

@app.route('/hi/<name>/')
def hi(name):
    print(name)
    print(id)
    return ' Hi ' + name

@app.route('/hi/<name>/<id>')
def name_id(name, id):
    print(name)
    print(id)
    return 'hi ' + name + ' ' + id

if __name__=="__main__":
    app.run(debug=True)
