from flask import Flask
app = Flask(__name__)
 
@app.route("/")
def hello():
    return "Welcome to Python Flask App!"


@app.route("/api")
def apiCall():
    return "api call"

if __name__ == "__main__":
    app.run()