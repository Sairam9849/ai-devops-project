from flask import Flask
import sys

app = Flask(__name__)

@app.route("/")
def home():
    print("ERROR: Something failed", file=sys.stderr)  # 
    return "Testing Error"

app.run(host="0.0.0.0", port=5000)
