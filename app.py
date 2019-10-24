from flask import Flask, render_template, request
from api import login, signup

app = Flask(__name__, template_folder='templates')

@app.route('/', methods = ['GET', 'POST'])
def index():
    return render_template('index.html')

@app.route('/signup_page', methods = ['GET', 'POST'])
def signup_page():
    while True:
        if request.method == 'GET':
            return render_template('signup.html', signupstatus = 'No info entered')
        elif request.method == 'POST':
            s = signup(email=request.form['signup-email'], password=request.form['signup-password'])
            if s[0] == 200:
                return render_template('signup.html', signupstatus = 'Successful!')
            elif s[0] == 400:
                return render_template('signup.html', signupstatus = 'Unsuccessful: ' + s[1])
            else:
                return render_template('signup.html', signupstatus = 'Unknown Error')

@app.route('/login_page', methods = ['GET', 'POST'])

def login_page():
    while True:
        if request.method == 'GET':
            return render_template('login.html', login = 'No information entered')
        elif request.method == 'POST':
            l = login(email=request.form['login-email'], password=request.form['login-password'])
            if l[0] == 200:
                print(l[1])
                return render_template('login.html', login = 'Successful!')
            elif l[0] == 400:
                return render_template('login.html', login = 'Unsuccessful: ' + l[1])
            elif l[0] == 'UNKNOWN':
                return render_template('login.html', login = 'Unknown error')


app.debug = True

app.run()