import os
import sys
from os import listdir
from flask import Flask, render_template, request, redirect, send_from_directory, send_file
app = Flask(__name__)

@app.route('/')
def index():
   return render_template('index.html')
   
if __name__ == '__main__':
   app.run(debug=True)