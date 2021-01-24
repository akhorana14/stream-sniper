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
@app.route('/sendUser', methods=['GET'])
def sendUser():
   if request.method == 'GET':
      user_name = request.args['id']
      streamers = getInfoFromAccount(user_name)
      s = []
      for streamer in streamers:
         for attr in streamer:
            s.append(attr)
      return render_template('sendStreamers.html',s1 = s[0], s2 = s[1], s3 = s[2], s4 = s[3], s5 = s[4], s6 = s[5], s7 = s[6], s8 = s[7], s9 = s[8], s10 = s[9], s11 = s[10], s12 = s[11], s13 = s[12], s14 = s[13], s15 = s[14])
@app.route('/uploadStreamer', methods=['POST'])
def sendStreamer():
   return '<p>Sent Streamers</p>'
   
if __name__ == '__main__':
   app.run(debug=True)