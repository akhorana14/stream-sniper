import os
import sys
from os import listdir
from flask import Flask, render_template, request, redirect, send_from_directory, send_file
app = Flask(__name__)

@app.route('/')
def index():
   return render_template('index.html')
@app.route('/index.html')
def ind():
   return render_template('index.html')
@app.route('/about.html')
def about():
   return render_template('about.html')
@app.route('/find.html')
def find():
   return render_template('find.html')
   
if __name__ == '__main__':
   app.run(debug=True)