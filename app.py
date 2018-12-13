#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Main runner function for the Flask app."""

from flask import Flask, render_template


app = Flask(__name__)


@app.route('/')
def hello_world():
    """Placeholder function for the Flask app."""
    return render_template("index.html")
