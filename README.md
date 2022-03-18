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

Requirements:
- Docker
- Chrome

## Sources

Githubs for libraries that enabled this project
- https://github.com/Uberi/speech_recognition

### Longer-term goals

- Create a nicer GUI on google chrome
- Allow for many different video on the same page
- Adapt the extension for any web browser
- Save a prebuilt image of the API on dockerhub
- Make infrastructure as code with terraform
- Add a button that reload the script on the page -- not necessary, it already check for new video every 5 sec until it find a video... maybe refresh it anyway after the first video is traduced to check for new video?


