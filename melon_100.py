import requests
from bs4 import BeautifulSoup

#멜론 TOP 100 List 크롤링
html = requests.get('http://www.melon.com/chart/index.htm').text
soup = BeautifulSoup(html, 'html.parser')
selt = '.wrap .wrap_song_info a[href*=playSong]'
tag_list = soup.select(selt)

for idx, tag in enumerate(tag_list, 1):
    print(idx, tag.text)
