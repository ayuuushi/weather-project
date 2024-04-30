from flask import *
import requests

app = flask(__app__)

@app.route('/', methods=["GET | POST"]
def serve_index():
  render_template("index.html")


if __name__ == 'main':
  app.run(port=5600)
