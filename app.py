import os
import sys
from os import listdir
from flask import Flask, render_template, request, redirect, send_from_directory, send_file
app = Flask(__name__)

@app.route('/')
def home():
   return render_template('index.html')
@app.route('/upload', methods=['POST'])
def upload_file():
   
   
   return send_file('download.ics')
   
if __name__ == '__main__':
   app.run(debug=True)