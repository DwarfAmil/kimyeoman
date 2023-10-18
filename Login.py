from flask import url_for, Flask, render_template, request, redirect

application = Flask(__name__)

application.run(host = "0.0.0.0")