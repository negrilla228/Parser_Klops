import requests
from bs4 import BeautifulSoup as b


def get_first_news():
    URL = 'https://klops.ru/'
    r = requests.get(URL)
    soup = b(r.text, 'html.parser')
    with open("news.txt","w") as file:

        news = soup.find_all('a', class_="item")
        for all_info_news in news:
            news_title = all_info_news.find('div', class_="title").text.strip()
            news_url = f'https://klops.ru{all_info_news.get("href")}'
            print(f"{news_title} | {news_url}")
            file.write(f"{news_title} | ")
            file.write(f"{news_url}\n")


get_first_news()