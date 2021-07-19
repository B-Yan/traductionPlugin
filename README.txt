Extension Project to help find specific words in audio content

The project is divided in 3 main parts
-The translator, which takes an .wav file and a word as input, then pulls out
the timestamp where the word was recognized in the .wav file

-The Scraper, which takes an URL and parse response to pick the audio content
of a web page. it gives its output to the translator

-The Extension package. Instructions for web browser to let it handle the
backend work of the scraper and the translator

Currently, development is aimed for Google Chrome compatibility
The scraper and the recognizer are to the basec functionning level

Development on Windows 10
Python version==3.7.9

Requirements:
-speech_recognition 	v:3.8.1
-pocketsphinx 		v:0.1.15
-youtube_dl		v:2021.6.6

Side programs
-ffmpeg			v:4.4
-swigwin		v:4.0.2

Notes:
Pocketsphinx requires you to install swigwin. The install is easy on windows,
but seems to requires a few extra steps on Linux
Ressources to install swigwin on Windows
https://stackoverflow.com/questions/44504899/installing-pocketsphinx-python-module-command-swig-exe-failed
https://www.youtube.com/watch?v=HDD9QqLtAws&ab_channel=AdlinLing

youtube_dl converts the AudioTrack from youtube to an mp3 using either ffmpeg or avprobe
Considering the options specified in scraper.py in ydl_opts, it uses ffmpeg, so be sure to
install it. Here is a tutorial to do it on windows. The moment it is unzipped, instead of adding it
to environment variables or else, add the ffmpeg.exe in the ffmpeg/bin to the same folder where the
youtube-dl.exe is located
https://www.youtube.com/watch?v=6kkYKhfbOMU&ab_channel=CrownGEEK

Githubs for libraries that enabled this project
https://github.com/Uberi/speech_recognition
https://github.com/ytdl-org/youtube-dl

goals in near future:
Generalize the scraping process to any website that contains a main audio file
Create a nice GUI on google chrome
adapt the extension for any web browser
make everything work in a single click