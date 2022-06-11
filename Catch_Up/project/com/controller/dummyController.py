from flask import request, render_template, redirect, url_for

from project import app

@app.route('/')
def userLogin():
    try:
        return '<h1>Hello! This is working!<h1>'
    except Exception as ex:
        print(ex)

