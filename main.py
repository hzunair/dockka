from flask import Flask, flash, redirect, render_template, request, session, abort

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello world! I am Hasib."

if __name__ == "__main__":
    #app.run()
    app.run(host='0.0.0.0', port=80)
