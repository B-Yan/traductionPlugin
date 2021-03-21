import speech_recognition as sr
import wave

# L'idée est de faire une boucle for pour analyser
# le contenu audio brin par brin avec un certain
# chevauchement entre les segments pour éviter les
# coupures

with sr.AudioFile('sample_phone_call_youtube.wav') as source:
    pass
    # r = sr.Recognizer()
    # r.energy_threshold = 300
    #
    # # Méthode pour aller chercher la durée totale du contenu?
    #
    # text_register = [] # On veut une liste avec un objet text et un index du segment analysé