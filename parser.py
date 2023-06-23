import requests

from bs4 import BeautifulSoup

print("Данный сервис позволяет получить ТОП-5 фильмов с сервисов IMDB:\n")
url = "https://www.imdb.com/search/title/?groups=top_100&sort=user_rating,desc"


headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.9; rv:45.0) Gecko/20100101 Firefox/45.0'
      }

response = requests.get(url, headers=headers)
html_content = response.content

soup = BeautifulSoup(html_content, 'html.parser')

films = soup.find_all('h3')
for film in films[:5]:
    print(film.find('a').text)
