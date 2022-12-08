# Student Registration System
import requests
import json
from flask import Flask, render_template

app = Flask(__name__)


@app.route("/template.html")
def home():
    response = requests.get("http://staging.bldt.ca/api/method/build_it.test.get_students")
    resp = response.text
    resp = json.loads(resp)

    # result = {}
    # result = resp['data']
    return render_template("template.html", **resp)


app.run(debug=True)