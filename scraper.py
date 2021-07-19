from __future__ import unicode_literals

import urllib3
import youtube_dl
from pydub import AudioSegment

# http = urllib3.PoolManager()
#
# r = http.request('GET', 'https://www.youtube.com/watch?v=rBhLJIPtosg&ab_channel=Aba%26Preach')
# data = r.data
# Gibberish and can't access to links in response
# print('data :', data)

# https://stackoverflow.com/questions/49246598/youtube-dl-get-audio-link-with-python
# Maybe change the preferredcodec directly to wav to skip a conversion

ydl_opts = {
    'format': 'bestaudio/best',
    'postprocessors': [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'wav',
        'preferredquality': '192',
    }],
    'outtmpl': '%(title)s.%(etx)s',
    'quiet': False
}
with youtube_dl.YoutubeDL(ydl_opts) as ydl:
    try:
        ydl.download(['https://www.youtube.com/watch?v=h2rR77VsF5c&ab_channel=TED-Ed'])
        # Will replace automatically the NA file if ffmpeg is properly installed
    except youtube_dl.postprocessor.ffmpeg.FFmpegPostProcessorError:
        # TODO: adapt the file name to get the .NA file in the folder
        AudioSegment.from_file('Does GEN Z SUCK.NA').export('audio_file.wav', format='wav')
    # TODO: store the file in a variable to pass in to the recognition.py module or merge \
    #  the files in one










# from selenium import webdriver
# from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.chrome.options import Options
#
# PATH = r"C:\Users\antoi\Desktop\chromedriver_win32 (1)\chromedriver.exe"
# # Si on veut ajouter un proxy, mais voir comment déterminer une adresse valide
# # PROXY = "127.63.13.19:3184" # Adresse au hasard?
# # chrome_options = webdriver.ChromeOptions()
# # chrome_options.add_argument('--proxy-server=%s' % PROXY)
# # driver = webdriver.Chrome(PATH, options=chrome_options)
#
# # Si on ne veut pas que le script lance de fenêtre à part, UTILE
# options = Options()
# options.headless = True
# driver = webdriver.Chrome(PATH, chrome_options=options)
#
# driver.get("https://www.reddit.com/")
# search = driver.find_element_by_name("q")
#
# search.send_keys("scraping")
# search.send_keys(Keys.RETURN)
#
# search_results = WebDriverWait(driver, 20).until(
#     EC.presence_of_element_located((By.CLASS_NAME, "rpBJOHq2PR60pnwJlUyP0"))
# )
#
# # 7 Getting the data in a list
# posts = search_results.find_elements_by_css_selector("h3._eYtD2XCVieq6emjKBH3m")
# print("data type of posts: ", type(posts))
#
# for post in posts:
#     header = post.find_element_by_tag_name("span")
#     print(header.text)
#
# # 8 Quitting the Browser
# driver.quit()

### YOUTUBE PART ###
import bs4

