#!/usr/bin/env python
# -*- coding: utf-8 -*-
from flask import Flask, render_template, request, jsonify
from boto import ec2
import os
app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/_get_regions')
def get_regions():
    regions = ec2.regions()
    return jsonify(regions=[r.name for r in regions])


@app.route('/_get_l_groups/<region>')
def get_log_groups():
    return ''

if __name__ == "__main__":
    app.run(
        port=int("5000"),
        debug=True
    )
