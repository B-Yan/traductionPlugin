# ControleFVoix

Extension Project to help find specific words in audio content

## Compatibility and requirements

Currently, development is aimed for Google Chrome compatibility

## Structure

The project is divided in 2 main parts:

- The translator, which takes an URL and a search string, download the file at that url, convert it to a .wav file and then pulls out the timestamp where the search string was recognized in the .wav file.

- The extension package, a small tool to extract video from a page and to prompt the user for a search string.

## Workflow

### How to install the plugin

1. Run the backend locally
2. Go to chrome://extensions on chrome
3. Click on the Developer mode checkbox
4. Click on Load Unpacked
5. Select the frontend folder of this project

### How to run the backend locally

1. Install Docker
2. Create a docker build (in terminal: docker build /PATH_TO_DOCKERFILE)
3. Run the docker (in terminal: docker run -P -d THE_IMAGE_NAME_GENERATED_BY_THE_BUILD)
    - -d make it run in a separeted terminal
    - the image name will be a random serie of character

## Sources

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

### Notes

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

## Sources

Githubs for libraries that enabled this project
https://github.com/Uberi/speech_recognition
https://github.com/ytdl-org/youtube-dl

## Short-term goals

Generalize the scraping process to any website that contains a main audio file
Create a nice GUI on google chrome
Adapt the extension for any web browser
Make everything work in a single click
