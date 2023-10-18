# 프로젝트 에스더

from flask import Flask, request, redirect
import random

app = Flask(__name__)

nextId = 4
Genshin_Impacts = [
    {'id':1,'title': '호두', 'body': '호두는...'},
    {'id':2,'title': '여행자', 'body': '여행자는...'},
    {'id':3,'title': '라이덴 쇼군', 'body': '라이덴 쇼군은...'},
]

def template(contents, content, id=None):
    contextUI = ''
    if id != None:
        contextUI = f'''
        <li><a href="/update/{id}/">update</a></li>
        <li><form action="/delete/{id}" method="POST"><input type="submit" value="delete"></form></li>
        '''
        
    return f'''<!doctype html>
    <html>
        <body>
            <h1><a href="/">원신</a></h1>
            <ol>
                {contents}
            </ol>
            {content}
            <ul>
                <li><a href="/create/">create</a></li>
                {contextUI}
            </ul>
        </body>
    </html>
'''

def getContents():
    liTags = ''
    for Genshin_Impact in Genshin_Impacts:
        liTags = liTags + f'<li><a href="/read/{Genshin_Impact["id"]}/">{Genshin_Impact["title"]}</a></li>'
    return liTags

@app.route('/')
def index():
    return template(getContents(), '<h2>Welcome</h2>Hello, WEB')


@app.route('/read/<int:id>/')
def read(id):
    title = ''
    body = ''
    for Genshin_Impact in Genshin_Impacts:
        if id == Genshin_Impact['id']:
            title = Genshin_Impact['title']
            body = Genshin_Impact['body']
            break
    return template(getContents(), f'<h2>{title}</h2>{body}', id)


@app.route('/create/', methods=['GET', 'POST'])
def create():
    if request.method == 'GET':
        content = '''
            <form action="/create/" method="POST">
                <p><input type="text"name="title" placeholder="title"></p>
                <p><textarea name="body" placeholder="body"></textarea></p>
                <p><input type="submit" value="create"></p>
            </form>
        '''
        return template(getContents(), content)
    elif request.method == 'POST':
        global nextId
        title = request.form['title']
        body = request.form['body']
        newGenshin_Impact = {'id': nextId, 'title': title, 'body': body}
        Genshin_Impacts.append(newGenshin_Impact)
        url = '/read/'+str(nextId)+'/'
        nextId = nextId + 1
        return redirect(url)
    

@app.route('/update/<int:id>/', methods=['GET', 'POST'])
def update(id):
    if request.method == 'GET':
        title = ''
        body = ''
        for Genshin_Impact in Genshin_Impacts:
            if id == Genshin_Impact['id']:
                title = Genshin_Impact['title']
                body = Genshin_Impact['body']
                break
        content = f'''
            <form action="/update/{id}/" method="POST">
                <p><input type="text"name="title" placeholder="title" value="{title}"></p>
                <p><textarea name="body" placeholder="body">{body}</textarea></p>
                <p><input type="submit" value="upedate"></p>
            </form>
        '''
        return template(getContents(), content)
    elif request.method == 'POST':
        title = request.form['title']
        body = request.form['body']
        for Genshin_Impact in Genshin_Impacts:
            if id == Genshin_Impact['id']:
                Genshin_Impact['title'] = title
                Genshin_Impact['body'] = body
                break
        url = '/read/'+str(id)+'/'
        return redirect(url)
    

@app.route('/delete/<int:id>/', methods=['POST'])
def delte(id):
    for Genshin_Impact in Genshin_Impacts:
        if id == Genshin_Impact['id']:
            Genshin_Impacts.remove(Genshin_Impact)
            break
    return redirect('/')


app.run(debug=True)