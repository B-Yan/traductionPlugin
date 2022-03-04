'''
A tool to read a wav file and to give the text with timestamp.

@author Antoine Marion, Yannick Bellerose
@version 2.0.0
'''

import speech_recognition as sr
import pocketsphinx
import pydub

OFFSET = 0
CHUNK_LEN = 4
OVERLAP = 1.5
ERROR_STRING = '' #is shown when there is no voice in the segment

'''
The idea is to parse an audio file by segment in a loop with an overlap between each segment to avoid the cuts.

@param filename the complete filename and path of the .wav file to treat (./myFile.wav)
@return a json representing the text of the video {"step": x, "content": ["Some text", "some other text", ...]} where X is the step lenght in seconds
'''
def getTimestampList(filename):
    actualOffset = OFFSET
    text_register = []
    completed = False
    file_length = 0

    while not completed:
        text = ""
        try:
            with sr.AudioFile(filename) as source:
                r = sr.Recognizer()
                file_length = source.DURATION
                # r.energy_threshold = 300 # if we have trouble getting clear audio 
                r.adjust_for_ambient_noise(source)
                audio = r.record(source, offset=actualOffset, duration=CHUNK_LEN)
                text = r.recognize_sphinx(audio_data=audio, language='en-US')  # , show_all=True) # Show All gives
        except sr.UnknownValueError as error:
            text = ERROR_STRING
        text_register.append("\""+text+"\"")
        print("INFO - CONTENT: " + str(actualOffset) + " - " + text)
        actualOffset += CHUNK_LEN - OVERLAP
        if (actualOffset) >= file_length:
            completed = True

    return "{\"step\":"+str((CHUNK_LEN-OVERLAP))+",\"list\":[" + ",".join(text_register) + "]}"