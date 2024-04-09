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
    
@app.route('/')
def home():
    years = get_year_options()
    #print(years)
    return render_template('page1.html', year_options=years)
    
@app.route('/showFact')
def render_fact():
    years = get_year_options()
    year = request.args.get('Year')
    return render_template('page1.html', year_options=years)
    
def get_year_options():
    with open('graduates.json') as graduates_data:
        major = json.load(graduates_data)
    years=[]
    for c in major:
        if c["Year"] not in years:
            year.append(c["Year"])
    options=""
    for s in years:
        options += Markup("<option value=\"" + s + "\">" + s + "</option>") #Use Markup so <, >, " are not escaped lt, gt, etc.
    return options
       
def is_localhost():
    """ Determines if app is running on localhost or not
    Adapted from: https://stackoverflow.com/questions/17077863/how-to-see-if-a-flask-app-is-being-run-on-localhost
    """
    root_url = request.url_root
    developer_url = 'http://127.0.0.1:5000/'
    return root_url == developer_url
    
if __name__=="__main__":
    app.run(debug=False)
