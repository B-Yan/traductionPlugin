import speech_recognition as sr
import pocketsphinx
import pydub

# L'idée est de faire une boucle for pour analyser
# le contenu audio brin par brin avec un certain
# chevauchement entre les segments pour éviter les
# coupures
OFFSET          = 0
CHUNK_LEN       = 10
OVERLAP         = 2
STEP            = CHUNK_LEN-OVERLAP
text_register   = [] # On veut une liste avec un objet text et un index du segment analysé
completed       = False
counter         = 0

def get_timestamp(text_register: list, input: str):
    # Check if the input substring can be found in the text_register strings
    timestamps_list = []
    # Go through each line of the text_register
    for i in range(len(text_register)):
        if text_register[i][1].find(input) != -1:
            # Add the index in text_register converted in seconds
            timestamps_list.append(i*STEP)
    return timestamps_list

# get user input
user_input = input('What word are you looking for?')

while not completed:
    # Will mark completed when total offset + duration will be > file_duration

    with sr.AudioFile('sample_phone_call_youtube.wav') as source:
        r = sr.Recognizer()
        file_length = source.DURATION  # float
        #r.energy_threshold = 300
        r.adjust_for_ambient_noise(source)
        # Meme si on ouvre le fichier audio, il faut quand même l'enregistrer dans la classe recognizer
        audio = r.record(source, offset=OFFSET, duration=CHUNK_LEN)

        text = r.recognize_sphinx(audio_data=audio, language='en-US') #, show_all=True) # Show All montre toutes \
        # les traductions probables du fichier
        print('text: ', text)
        OFFSET += STEP

        if OFFSET + CHUNK_LEN > file_length:
            completed = True
            break
    counter += 1
    text_register.append([counter, text])

timestamps_list = get_timestamp(text_register, user_input)
if not timestamps_list:
    print('no matches!')
else:
    print('matches at: ', timestamps_list)


