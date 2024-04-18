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

"""@app.route('/majors')
def home():
    majors = get_majors_options()
    #print(years)
    return render_template('page1.html', major_options=majors)"""

@app.route('/highestSalaries')
def render_highest_sal():
    with open('graduates.json') as salaries_data:
        data = json.load(salaries_data)
    year = request.args['year']   
    major = "Chemistry"
    sal = 0
    for s in data:
        if s["Year"] == year and s["Salaries"] > sal:
            sal = s["Salaries"]
            state = s["major"]
    return render_template('page1.html', major = major)

    
"""def get_major_options():
    with open('graduates.json'):
        json.load('graduates.json')
    options=""
    return options"""
    
    

def is_localhost():
    root_url = request.url_root
    developer_url = 'http://127.0.0.1:5000/'
    return root_url == developer_url
    
if __name__=="__main__":
    app.run(debug=False)
