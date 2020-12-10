from flask import Flask
app = Flask(__name__)


#use the route decorator to bind a function to a URL
@app.route('/hello')
def hello_world():
    return 'Hello, Angels!'

@app.route('/')
def index():
	return 'Index Page'
	
