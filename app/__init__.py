from flask import Flask

app = Flask(__name__)
from app import webhook
app.static_folder = 'static'
