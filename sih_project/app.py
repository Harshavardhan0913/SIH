from flask import *
from database import WorkspaceData

import requests
from bs4 import BeautifulSoup

app = Flask(__name__)

@app.route('/')
def home():
    return render_template("home.html")

@app.route('/login')
def login():
    db = WorkspaceData()
    return render_template("login.html", retry=False, errorType='none')

@app.route('/validate_login', methods=['POST', 'GET'])
def validate_login():
    if request.method == 'POST':
        if 'login' in request.form:
            user_name = request.form.get('user')
            password = request.form.get('pass')
            db = WorkspaceData()
            data = db.get('login', user_name)
            for s in data:
                if user_name == s[0] and password == s[1]:
                    return redirect('/')
            return render_template('login.html', retry=True, errorType='login')
        elif 'signup' in request.form:
            user_name = request.form.get('user')
            password = request.form.get('pass1')
            email = request.form.get('email')
            db = WorkspaceData()
            db.add('login',[(user_name, password, email,"student")])
            return render_template('login.html', retry=False,errorType='none')

@app.route('/profile')
def profile():
    db = WorkspaceData()
    return render_template("profile.html")

@app.route('/hackathon')
def hackathon():
    db = WorkspaceData()
    data = db.get_hackathons()


    url = "https://www.hackerearth.com/challenges/hackathon/"
    r = requests.get(url)
    htmlcontent = r.content
    soup = BeautifulSoup(htmlcontent, 'html.parser')
    headings = soup.find_all('span', class_="challenge-list-title challenge-card-wrapper")
    for link in headings:
        t = {}
        t['name'] = link.get_text()
        t['date'] = 'live'
        t['location'] = 'online'
        #print(link.get_text())
        data.append(t)


    return render_template("wel.html",hackathons = data,l=1)
@app.route('/workshops')
def workshops():
    return render_template("workshops.html")


if __name__ == '__main__':
    app.run()
