
#Author: Noah Ahmed
#Date: 11/12/19
#Description: A web application that asks users whether they are
#          interested in reading an article that is randomly
#          chosen. If they aren't interested, they can try again.

from flask import Flask, render_template, flash, redirect
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
import requests

app = Flask(__name__)
app.config['SECRET_KEY'] = 'csumb-otter'
bootstrap = Bootstrap(app)



@app.route('/', methods=['GET','POST'])
def home():
    S = requests.Session()

    URL = "https://en.wikipedia.org/w/api.php"

    PARAMS = {
        "action": "query",
        "format": "json",
        "list": "random",
        "rnlimit": "1",
        "rnnamespace": "0"
    }

    R = S.get(url=URL, params=PARAMS)
    DATA = R.json()

    RANDOMS = DATA["query"]["random"]
    title = RANDOMS[0]["title"]
    linkT = title.replace(' ','_')
    return render_template('index.html', linkT=linkT, title=title)
