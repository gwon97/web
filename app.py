from flask import Flask
import os
import subprocess

app = Flask(__name__)

@app.route("/")
def home():
    return "Hello from Flask on Koyeb!"

@app.route("/whoami")
def whoami():
    result = subprocess.run(["whoami"], stdout=subprocess.PIPE)
    return f"Running as: {result.stdout.decode()}"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))
