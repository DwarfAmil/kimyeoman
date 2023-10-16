# 프로젝트 에스더

from flask import Flask
import random

app = Flask(__name__)

Genshin_Impacts = [
    {'id':1,'title': '호두', 'body': '호두는...'},
    {'id':2,'title': '여행자', 'body': '여행자는...'},
    {'id':3,'title': '라이덴 쇼군', 'body': '라이덴 쇼군은...'},

]

@app.route('/')
def index():
    liTags = ''
    for Genshin_Impact in Genshin_Impacts:
        liTags = liTags + '<li>'+Genshin_Impact['title']+'</li>'
    return '''<!doctype html>
    <html>
        <body>
            <h1><a href="/">원신</a></h1>
            <ol>
                liTags
            </ol>
            <h2>Welcome</h2>
            대충 원신 캐릭터 설명
        </body>
    </html>
'''


@app.route('/create')
def create():
    return 'Create'


@app.route('/read/<id>/')
def read(id):
    print(id)
    return 'Read '+id


app.run(port=5001, debug=True)