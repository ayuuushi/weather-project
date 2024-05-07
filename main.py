from flask import *
import requests

app = flask(__name__)

@app.route('/', methods=["GET",  "POST"])
def serve_index():
  return render_template("index.html")


if __name__ == 'main':
  app.run(port=5600)
