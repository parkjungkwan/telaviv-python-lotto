from bs4 import BeautifulSoup
import re


def read_file():
    file = open('C:/consumer_reports.txt',
                "rt",
                encoding='UTF-8'
                )
    data = file.read()
    file.close()
    return data

soup = BeautifulSoup(read_file(),'lxml')
products = {}   # product name - key product link - value


product_names = [div.div.a.span.string for div in soup.find_all('div',class_='entry-letter')]

product_links = [div.div.a['href'] for div in soup.find_all('div',class_='entry-letter')]

products = {div.div.a.span.string:div.div.a['href'] for div in soup.find_all('div',class_='entry-letter')}

for key,value in products.items():
    print(key , '   -->',value)

