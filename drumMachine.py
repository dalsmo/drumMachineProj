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

drumList = [];


@app.before_first_request
def _run_on_start():
    for root, dirs, files in os.walk("./drums/",followlinks=False):
        for file in files:
            if file.endswith(('mp3','wav')):
                drumList.append(os.path.join(root, file))

class View(flask.views.MethodView):
    def get(self):
        print "---------------------------------------------------"
        playing = random.choice(drumList)
        p = vlc.MediaPlayer(playing)
        p.play()
        print "playing sound: " + playing
        return "<br>\n".join(drumList)
    
    def put(self):
        print "---------------------------------------------------"
        parsed_json = json.loads(request.data)
        if parsed_json['drum'] in drumList:
            print "playing sound: " + parsed_json['drum']
            p = vlc.MediaPlayer(parsed_json['drum'])
            p.play()
            return "playing sound: " + parsed_json['drum']
        else: 
            print "sound not in list, try another"
            return "sound not in list, try another"


app.add_url_rule('/',view_func=View.as_view('main'))


app.debug = True
app.run()
#app.run(host='0.0.0.0',port=12345)

#if __name__ == '__main__':
#    app.run()







