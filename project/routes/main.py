from flask import Flask, Blueprint, render_template

main = Blueprint('main', __name__)


@main.route('/')
def index():
    return render_template('main.html')
