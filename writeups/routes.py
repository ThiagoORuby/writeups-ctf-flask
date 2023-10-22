from flask import render_template, redirect, url_for, flash, send_from_directory
from flask import current_app as app
from markdown import markdown
from markdown.extensions import *
import os

basedir = os.path.abspath(os.path.dirname(__file__))

@app.route("/", methods=["GET", "POST"])
def index():
    # Lê o arquivo Markdown

    files = os.listdir(os.path.join(basedir, 'static/markdown'))
    files = [file for file in files if ".md" in file]

    return render_template('index.html', files = files)

@app.route("/<filename>")
def writeup(filename):

    content = open(os.path.join(basedir, f'static/markdown/{filename}'), 'r', encoding="utf-8")
    md = markdown(content.read(), 
                  extensions=['fenced_code', 'tables', 'codehilite', 'extra', 'attr_list'])
    
    return render_template('writeup.html', md = md, filename=filename[:-3])