import os
import sys
from os import listdir
from flask import Flask, render_template, request, redirect, send_from_directory, send_file
from StreamScraper import getRecommendations, getInfoFromAccount
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
@app.route('/sendUser', methods=['GET','POST'])
def sendUser():
   if request.method == 'POST':
      print(request.data)
      user_name = request.form['id']
      print(user_name + "\n\n\n\n\n\n\n\n\n")
      return getRecommendations(user_name)
@app.route('/uploadStreamer', methods=['POST'])
def sendStreamer():
   return '<p>Sent Streamers</p>'
   
if __name__ == '__main__':
   app.run(debug=True)