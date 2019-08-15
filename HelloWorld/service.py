from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
	return "Hello World!/n"
	
@app.route("/user/<username>")
def show_user(username):
	return "Hello {}".format(username)
	
	
if __name__ == "__main__":
	app.run(host='0.0.0.0')
	
