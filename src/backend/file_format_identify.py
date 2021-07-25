'''
Take an URL and pulls the format
'''

import moviepy.editor as mp
import re
from pydub.utils import _fd_or_path_or_tempfile
import requests
from pydub import AudioSegment

r = requests.get('https://dms.licdn.com/playlist/C4D0DAQGMdkc4SNOmvw/learning-original-video-vbr-540/0/1623699034346?e=1627322400&v=beta&t=KAm97tqEbCIY6ojMfvYuyS_U3F9PurpLS7rhal0IIWM')
file_type = r.headers['Content-Type']
# pulls str of extension
file_extension = file_type[6:]

with open(f'video_test_file.{file_extension}', 'wb') as f:
    f.write(r.content)
    f.close

# TODO: check why file isn't saved in right place
print(f'video_test_file.{file_extension}')
wav_file = AudioSegment.from_file('video_test_file.mp4', 'mp4')# .extract('wav_file.wav', format='wav')


