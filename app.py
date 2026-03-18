from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    print("error occurred")   
    return "Testing Error"

app.run(host="0.0.0.0", port=5000)
