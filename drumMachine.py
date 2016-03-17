import flask , flask.views
import vlc
import time
import os
import random
from flask import request
import json

app = flask.Flask(__name__)

#https://www.youtube.com/watch?v=iSrZ6r7hwdM&list=PL0DA14EB3618A3507
# . venv/bin/activate

def getDrums():
    fileList = [];
    for root, dirs, files in os.walk("./drums/"):
        for file in files:
            if file.endswith(('mp3','wav')):
                fileList.append(os.path.join(root, file))
    return fileList

class View(flask.views.MethodView):
    def get(self):
        print "---------------------------------------------------"
        drumList = getDrums()
        playing = random.choice(drumList)
        p = vlc.MediaPlayer(playing)
        p.play()
        print "playing sound: " + playing
        return "<br>\n".join(drumList)
    
    def put(self):
        print "---------------------------------------------------"
        parsed_json = json.loads(request.data)
        print "playing sound: " + parsed_json['drum']
        p = vlc.MediaPlayer(parsed_json['drum'])
        p.play()
        return "playing sound: " + parsed_json['drum']


app.add_url_rule('/',view_func=View.as_view('main'))


app.debug = True
app.run()







