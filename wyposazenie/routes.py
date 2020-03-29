from flask import render_template, url_for, flash, redirect, request
from wyposazenie import app
@app.route('/')
def hello_world():
    return 'Bart'