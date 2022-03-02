from flask import Flask, request
import requests
import os
from pydub import AudioSegment
from recognition import *
app = Flask(__name__)

@app.route('/',methods = ['GET'])
def getHelloWorld():
    return "helloworld"

@app.route('/',methods = ['POST'])
def get_video():
    URL = request.get_json()["URL"]
    print("INFO - URL: " + URL)
    WAVNAME = "audiofile.wav"
    name = getFilename(URL)
    getResponse(URL, name[0])
    AudioSegment.from_file(name[0], name[1]).export(WAVNAME, format='wav')
    os.remove(name[0])
    timestamp_list = getTimestampList(WAVNAME)
    os.remove(WAVNAME)
    return timestamp_list

def getResponse(URL, filename):
    response = requests.get(URL)
    file = open(filename, "wb")
    file.write(response.content) #TODO here file and response are open, potential ram issue -> stream
    file.close()
    response.close()

def getFilename(URL):
    name = URL.split("/")
    name = name[len(name)-1]
    name = name.split(".")
    name[0] = name[0] + "." + name[1]
    return name
    
if __name__=="__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(debug=True, host='0.0.0.0', port=port)