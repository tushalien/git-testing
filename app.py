from flask import Flask 

app = Flask(__name__)

@app.route('/')
def home():
	return "Hello World!!"

@app.route('/tushar')
def tushar():
	return "Hello Tushar"

@app.route('/<name>')
def name(name):
	return "Hello %s" % name



app.run(host='0.0.0.0', port =8000)