# -*- coding: utf-8 -*-
"""app

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1cAlrK1cInEuDeavDJtKPt4R1s3w37JNr
"""

from flask import Flask, request, render_template

app = Flask(__name__)

from textblob import TextBlob
from transformers import pipeline

classifier = pipeline('sentiment-analysis', "mrm8488/bert-small-finetuned-squadv2")

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        text = request.form.get("text")
        print(text)
        r1 = TextBlob(text).sentiment
        r2 = classifier(text)
        return(render_template("index.html", result1=r1, result2=r2))
    else:
        return(render_template("index.html", result1="2", result2="2"))

if __name__ == "__main__":
    app.run()