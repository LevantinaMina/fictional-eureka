import requests
from bs4 import BeautifulSoup
import pandas as pd

def cate():
    data = []


    url = 'https://books.toscrape.com/catalogue/category/books/travel_2/index.html'
    html_content = requests.get(url).text
    soup = BeautifulSoup(html_content, 'lxml')

    entries = soup.find_all('article', class_='product_pod')


    for entry in entries:
        product_name = entry.find('h3').find('a')['title']
        price_element = entry.find('p', class_='price_color').text.strip()
        price = price_element.replace('Â', '')

        rating_element = entry.find('p', class_='star-rating')
        rating = rating_element['class'][1]

        data.append({'product_name': product_name, 'price': price, 'rating': rating})

    return data

books = cate()

df = pd.DataFrame(books)

df.to_excel('book.xlsx')

print(df)