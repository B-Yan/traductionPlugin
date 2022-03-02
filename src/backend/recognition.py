import speech_recognition as sr
import pocketsphinx
import pydub

'''
The idea is to parse an audio file by segment in
a loop with an overlap between each segment to avoid
the cuts
'''
OFFSET = 0
CHUNK_LEN = 4
OVERLAP = 1.5
ERROR_STRING = 'NoWordsErrorString'

def getTimestampList(filename):
    actualOffset = OFFSET
    text_register = []
    i=0
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
        content = "{\"time\":\""+str(actualOffset)+"\",\"content\":\""+text+"\"}"
        text_register.append(content)
        print("INFO - CONTENT: " + content)
        actualOffset += CHUNK_LEN - OVERLAP
        if (actualOffset + CHUNK_LEN) > file_length:
            completed = True

    return "{\"list\":[" + ",".join(text_register) + "]}"