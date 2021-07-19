import speech_recognition as sr
import pocketsphinx
import pydub

# The idea is to parse an audio file by segment in
# a loop with an overlap between each segment to avoid
# the cuts
OFFSET = 0  # Tunable parameter
CHUNK_LEN = 4  # Tunable parameter
OVERLAP = 1.5  # Tunable parameter
STEP = CHUNK_LEN - OVERLAP
text_register = []  # List with an index and the words associated with the index segment
completed = False
counter = 0


def get_timestamp(text_register: list, input: str):
    # Check if the input substring can be found in the text_register strings
    timestamps_list = []
    # Go through each line of the text_register
    for i in range(len(text_register)):
        if text_register[i][1].find(input) != -1:
            # Add the index in text_register converted in seconds
            timestamps_list.append((i + 1) * STEP)
    return timestamps_list


# get user input
# TODO: Set all code below in a function to run from the main file
user_input = input('Which word are you looking for?')

while not completed:
    # Will mark completed when total offset + duration will be > file_duration
    try:
        # TODO: Use a parameter to search for the .wav file in the folder
        with sr.AudioFile('Why is it so hard to cure cancer - Kyuson Yun.wav') as source:
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
            print('progression: ', {(CHUNK_LEN-OVERLAP)*i/file_length*100} '%')
            OFFSET += STEP

            if OFFSET + CHUNK_LEN > file_length:
                completed = True
                break
            counter += 1
            text_register.append([counter, text])

    except sr.UnknownValueError as error:
        print('Speech unintelligible or no words at all in this chunk')
        OFFSET += STEP

        if OFFSET + CHUNK_LEN > file_length:
            completed = True
            break
        counter += 1
        text_register.append([counter, 'NoWordsErrorString'])
        pass

timestamps_list = get_timestamp(text_register, user_input)
if not timestamps_list:
    print('no matches!')
else:
    print(f'matches for {user_input} at: ', timestamps_list)
