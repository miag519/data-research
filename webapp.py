from flask import Flask, url_for, render_template
from markupsafe import Markup

import os
import json


app = Flask(__name__)

@app.route("/")
def render_main():
    return render_template('home.html')

@app.route("/p1")
def render_page1():
    return render_template('page1.html')

@app.route("/p2")
def render_page2():
    return render_template('page2.html')

@app.route('/p1')
def home():
    majors = get_majors_options()
    #print(years)
    return render_template('page1.html', major_options=majors)

@app.route('/Major')
def render_fact():
    majors = get_major_options()
    return render_template('page1.html', major_options=majors)
    
def get_major_options():
    with open('graduates.json') as graduates_data:
        majors = json.load(graduates_data)
    major=[]
    for c in majors:
        if c["Major"] not in major:
            majors.append(c["Major"])
    options=""
    for s in major:
        options += Markup("<option value=\"" + s + "\">" + s + "</option>") #Use Markup so <, >, " are not escaped lt, gt, etc.
    return options
    
    

def is_localhost():
    root_url = request.url_root
    developer_url = 'http://127.0.0.1:5000/'
    return root_url == developer_url
    
if __name__=="__main__":
    app.run(debug=False)
