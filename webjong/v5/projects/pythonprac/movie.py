import requests
from bs4 import BeautifulSoup
from pymongo import MongoClient

client = MongoClient("내 URL")
db = client.dbsparta

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
data = requests.get(
    'https://movie.naver.com/movie/sdb/rank/rmovie.naver?sel=pnt&date=20210829', headers=headers)

soup = BeautifulSoup(data.text, 'html.parser')

# old_content > table > tbody > tr:nth-child(3) > td.title > div > a
# old_content > table > tbody > tr:nth-child(4) > td.title > div > a

movies = soup.select('#old_content > table > tbody > tr')

for movie in movies:
    a = movie.select_one('td.title > div > a')
    if a is not None:
        title = a.text
        rank = movie.select_one('td:nth-child(1) > img')['alt']
        star = movie.select_one('td.point').text
        # print(rank, title, star)
        doc = {
            'rank': rank,
            'title': title,
            'star': star
        }
        # db.movies.insert_one(doc)

# Q1
target_movie = db.movies.find_one({'title': '가버나움'})
print(target_movie['star'])

# Q2
target_movie = db.movies.find_one({'title':'가버나움'})
target_star = target_movie['star']

movies = list(db.movies.find({'star':target_star}))

for movie in movies:
    print(movie['title'])

# Q3
db.movies.update_one({'title':'가버나움'},{'$set':{'star':'0'}})