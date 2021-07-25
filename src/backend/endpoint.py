'''

'''

from flask import Flask
import requests
import pydub import AudioSegment
# from flask_restful

app = Flask(__name__)

@app.route('/<URL>')
def get_video(URL):
    '''
    takes an URL as imput and return the timestamp_list from the translation

    1- Download from URL
    '''
    file = requests.get(URL) # file format: file.
    # TODO: Identify format
    file_type = file.headers['Content-Type']
    file_extension=

    wav_file = AudioSegment.from_file(f"<file_name.{format}>").export('audiofile.wav', format='wav')

    # return a list of timestamp
    return timestamp_list



if __name__=="__main__":
    app.run(debug=True)