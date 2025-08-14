from flask import Flask, request

app = Flask(__name__)

@app.route("/")
def index():
    name = request.args.get("name", "")
    return f"<h1>Welcome, {name}</h1>"  # XSS vulnerability here

if __name__ == "__main__":
    app.run(debug=True)
