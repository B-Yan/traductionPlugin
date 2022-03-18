'''
A tool to read a wav file and to give the text with timestamp.

@author Antoine Marion, Yannick Bellerose
@version 2.0.0
'''

import speech_recognition as sr
import pocketsphinx
import pydub

import threading
import multiprocessing
import time
import concurrent.futures as cf
import numpy as np


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



# get user input
# TODO: Set all code below in a function to run from the main file
user_input = input('Which word are you looking for?')

while True:
    # Will mark completed when total offset + duration will be > file_duration
    try:
        # TODO: Use a parameter to search for the .wav file in the folder
        with sr.AudioFile('../example/WhyHard.wav') as source:
            r = sr.Recognizer()
            file_length = source.DURATION  # float
            # r.energy_threshold = 300 # if we have trouble getting clear audio
            r.adjust_for_ambient_noise(source)
            # Even if we open the file, we need to create an audio object by recording
            audio = r.record(source, offset=OFFSET, duration=CHUNK_LEN)

            text = r.recognize_sphinx(audio_data=audio, language='en-US')  # , show_all=True) # Show All gives
            # all possible translations
            # Throws an exception if no words or not gibberish type speech_recognition.UnknownValueError
            print('text: ', text)
            # print('progression: ', {(CHUNK_LEN-OVERLAP)*i/file_length*100} '%')
            OFFSET += STEP

            if OFFSET + CHUNK_LEN > file_length:
                break
            counter += 1
            text_register.append([counter, text])

    except sr.UnknownValueError as error:
        print('Speech unintelligible or no words at all in this chunk')
        OFFSET += STEP

        if OFFSET + CHUNK_LEN > file_length:
            break
        counter += 1
        text_register.append([counter, 'NoWordsErrorString'])
        pass


    return "{\"step\":"+str((CHUNK_LEN-OVERLAP))+",\"list\":[" + ",".join(text_register) + "]}"




# Get the length before the while loop to set a for loop instead
def GetFileLength(filename_):
    # Returns file length as int [seconds]
    with sr.AudioFile(filename_) as source:
        return source.DURATION


# attempt to multi process the loop. Call this method as target for MultiProcess librairies
def MultiProcessRecognition(filename_, localOffset_):
    # Use of multiprocess instead of thread because CPU bound task
    try:
        with sr.AudioFile(filename_) as source:
            r = sr.Recognizer()
            audio = r.record(source, offset=localOffset_, duration=CHUNK_LEN)
            text = r.recognize_sphinx(audio_data=audio, language='en-US')
    except sr.UnknownValueError as error:
        text = ERROR_STRING
    return (text, localOffset_)

def OffsetListCreate(numberOfThreads_):
    # list of localOffset_ args for MultiProcessRecognition
    return np.array([OFFSET*(i+1) for i in range(numberOfThreads_)])

def SortTextRegister(textRegister_):
    # Sorts based on offset value
    return textRegister.sort(key=lambda x: x[1])

   
textRegister = []
def main():
    # https://www.webucator.com/article/python-clocks-explained/
    # Plus fiable que time(), plus précis que process_time()
    startTime = time.perf_counter()
    
    filePath = r"C:\Users\antoi\Desktop\Github\Russias_war_in_Ukraine_enters_its_(getmp3.pro)"
    fileLength = GetFileLength(filePath)
    numberOfThreads = int(fileLength/CHUNK_LEN)
    offsetList = OffsetListCreate(numberOfThreads)

    with cf.ProcessPoolExecutor() as executor:
        #TODO: Specify offset list argument from for loop
        results = [executor.submit(MultiProcessRecognition, localOffset_) for localOffset_ in offsetList]

        for f in cf.as_completed(results):
            textRegister.append(f.result())

    textRegister = SortTextRegister(textRegister)

    endTime = time.perf_counter()
    print('execution time [sec]: ', endTime - startTime)
    print('Text register: ', textRegister)
    


if __name__ == '__main__':
    main()

