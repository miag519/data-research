from flask import Flask, url_for, render_template

app = Flask(__name__) #__name__ = "__main__" if this is the file that was run.  Otherwise, it is the name of the file (ex. webapp)

@app.route("/")
def render_main():
    return render_template('home.html')

@app.route("/p1")
def render_page1():
    return render_template('page1.html')

@app.route("/p2")
def render_page2():
    return render_template('page2.html')
    
@app.route('/HighestSalaries')
def render_fact():
    years = get_year_options()
    #print(years)
    year = request.args.get('year')
    return render_template('page1.html', year_options=years)
    
def get_year_options():
    with open('graduates.json') as graduates_data:
        salaries = json.load(graduates_data)
    years=[]
    for c in salaries:
        if c["Year"] not in years:
            years.append(c["Year"])
    options=""
    for s in years:
        options += Markup("<option value=\"" + s + "\">" + s + "</option>") #Use Markup so <, >, " are not escaped lt, gt, etc.
    return options
    
"""@app.route('/buisness')
def render_fact():
    
    employment = request.args.get('employment')
    return render_template('page2.html')"""

def is_localhost():
    root_url = request.url_root
    developer_url = 'http://127.0.0.1:5000/'
    return root_url == developer_url
    
if __name__=="__main__":
    app.run(debug=False)
