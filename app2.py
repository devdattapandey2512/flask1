from flask import Flask


app = Flask(__name__)

@app.route("/home")

def home():
	return "this is home page"

@app.route("/<Name>")

def Dynamic(Name):
	return f"Hey {Name}"

if __name__ == "__main__":
	app.run(debug = True)