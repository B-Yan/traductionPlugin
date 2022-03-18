FROM ubuntu:latest
WORKDIR /usr/src/app
COPY . .
ENV DEBIAN_FRONTEND=noninteractive 
RUN apt-get update -y
RUN apt-get install -y gcc python3 python3-all-dev python3-pip build-essential swig git libpulse-dev libasound2-dev ffmpeg
RUN python3 -m pip install --upgrade pip setuptools wheel
RUN pip3 install --no-cache-dir -r requirements.txt
EXPOSE 5000
CMD [ "python3", "./endpoint.py" ]