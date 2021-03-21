import speech_recognition as sr
import pocketsphinx

# L'idée est de faire une boucle for pour analyser
# le contenu audio brin par brin avec un certain
# chevauchement entre les segments pour éviter les
# coupures

text_register = [] # On veut une liste avec un objet text et un index du segment analysé

with sr.AudioFile('sample_phone_call_youtube.wav') as source:

    try:
        r = sr.Recognizer()
        r.energy_threshold = 300

        # Meme si on ouvre le fichier audio, il faut quand même l'enregistrer dans la classe recognizer
        audio = r.record(source)

        source.DURATION # float de la durée
        text = r.recognize_sphinx(audio_data=audio, language='en-US')
        print(text)

    finally:
        print('Program stopping')