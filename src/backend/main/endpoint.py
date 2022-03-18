'''
A flask controller that serve request. It's the starting point of the application

@author Yannick Bellerose
@version 1.0.0
'''

from flask import Flask, request
from flask_cors import CORS
import requests
import os
import youtube_dl
import random
import string
from pydub import AudioSegment
from recognition import *
app = Flask(__name__)
CORS(app)

'''
The default endpoint it show a small text to describe how to use this API
'''
@app.route('/',methods = ['GET'])
def getHelloWorld():
    return "Welcome to controleFVoix a tool to extract the text with timestamp, to use it call this same endpoint but with a post request respecting the following format: {\"URL\":\"https://www.w3schools.com/html/mov_bbb.mp4\"}"

'''
The POST endpoint transforming a video to an array where each part are the same length

@param body {"URL":"theUrlOfYourVideo"}
@return a json representing the text of the video {"step": x, "content": ["Some text", "some other text", ...]} where X is the step lenght in seconds
'''
@app.route('/',methods = ['POST'])
def get_video():
    URL = request.get_json()["URL"]
    print("INFO - URL: " + URL)
    WAVNAME = ''.join(random.SystemRandom().choice(string.ascii_letters + string.digits) for _ in range(25)) + ".wav"
    name = []
    if "youtube.com" in URL:
        youtubeURL(URL, WAVNAME)
    elif "dailymotion.com" in URL:
        dailymotionURL(URL)
    elif "vimeo.com" in URL:
        vimeoURL(URL)
    else:
        defaultURL(URL, WAVNAME)
    timestamp_list = getTimestampList(WAVNAME)
    os.remove(WAVNAME)
    return timestamp_list

def youtubeURL(URL, WAVNAME):
    ydl_opts = {
        'format': 'bestaudio/best'
    }
    filename = ""
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(URL, download=True)
        filename = ydl.prepare_filename(info)
    name = getFilename(filename)
    AudioSegment.from_file(name[0], name[1]).export(WAVNAME, format='wav')
    os.remove(name[0])

def dailymotionURL(URL):
    raise Exception("Dailymotion not yet implemented")

def vimeoURL(URL):
    raise Exception("Vimeo not yet implemented")

def defaultURL(URL, WAVNAME):
    name = getFilename(URL)
    getResponse(URL, name[0])
    AudioSegment.from_file(name[0], name[1]).export(WAVNAME, format='wav')
    os.remove(name[0])

'''
A simple function that download a file and write it to the disk

@param URL the url of the file to download
@param filename the name (and the path if required) you want the file to have
'''
def getResponse(URL, filename):
    response = requests.get(URL)
    file = open(filename, "wb")
    file.write(response.content) #TODO here file and response are open, potential ram issue -> stream
    file.close()
    response.close()

'''
A function that receive a complete url and return an array containing the name with the extension, and the extension

@param URL the url of a file you want the name or extension
@return an array containing [0] the name of the file (including the extension) [1] the extension of the file
'''
def getFilename(URL):
    name = URL.split("/")
    name = name[len(name)-1]
    name = name.split(".")
    name[0] = name[0] + "." + name[1]
    return name

if __name__=="__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(debug=True, host='0.0.0.0', port=port)