import requests
from bs4 import BeautifulSoup
from pymongo import MongoClient

client = MongoClient('localhost', 27017)
db = client.dbsparta

headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
data = requests.get('https://www.genie.co.kr/chart/top200?ditc=D&rtm=N&ymd=20200713',headers=headers)

soup = BeautifulSoup(data.text, 'html.parser')

#body-content > div.newest-list > div > table > tbody > tr:nth-child(1) > td.info > a.title.ellipsis

musics = soup.select('#body-content > div.newest-list > div > table > tbody > tr')


for music in musics:
    # movie 안에 a 가 있으면,
    a_tag = music.select_one('td.info > a')
    if a_tag is not None:
        raw_rank = music.select_one('td.number').text
        rank = (raw_rank.strip()[0:2]).strip()

        raw_title = music.select_one('td.info > a.title.ellipsis').text
        title = raw_title.strip()

        singer = music.select_one('td.info > a.artist.ellipsis').text

        print(rank, title, singer)
        doc = {
            'rank': rank,
            'title': title,
            'singer': singer
        }
        db.musics.insert_one(doc)
