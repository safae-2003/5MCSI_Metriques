from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return "Hello from Alwaysdata & Github Actions 🚀"

if __name__ == "__main__":
    app.run()
