#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# A very simple Flask Hello World app for you to get started with...

import flask
from flask import Flask, request

app = Flask(__name__, static_folder="static", static_url_path="", template_folder="templates")


@app.context_processor
def inject_globals():
    return {
        "isclever": [
            "да",
            "нет",
            "наверное"
        ]
    }

@app.route('/')
def root():
    return flask.render_template(
        'index.html'
    )


@app.route('/game', methods = ['GET', 'POST'])
def hello_name():
    if request.method == 'GET':
        name_param=request.args.get('name')
    elif request.method == 'POST':
        name_param=request.form.get('name')

    if name_param is None:
        name_param="Неопределен"

    return flask.render_template(
        'supr.html',
        name=name_param,
        method=request.method
    )

if __name__ == '__main__':
   app.run(debug = True)