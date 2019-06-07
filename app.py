#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Main runner function for the Flask app."""

from flask import Flask, render_template, request


app = Flask(__name__)


@app.route('/')
def hello_world():
    """Test the Flask app."""
    return render_template("index.html")


@app.route("/upload", methods=["POST"])
def upload():
    uploaded_files = request.files.getlist("file[]")
    print(uploaded_files)
    return render_template("upload.html", files=uploaded_files)
