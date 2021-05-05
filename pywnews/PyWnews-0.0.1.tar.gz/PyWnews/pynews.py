import requests
from bs4 import BeautifulSoup
URL = 'https://apnews.com/hub/ap-top-news'
page = requests.get(URL)
soup = BeautifulSoup(page.content, 'html.parser')
class wnews:
  def news(self):
    news = []
    for div in soup.find_all(class_='FeedCard', attrs = {'class' : 'Component-h1'}):
      for h in div.find('h1'):
        new = h
        if new not in news:
          news.append(new)
    print(news)