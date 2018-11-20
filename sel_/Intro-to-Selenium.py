from selenium import webdriver      # imports
from time import sleep
from bs4 import BeautifulSoup

driver = webdriver.Chrome('C:/Users/1027/source/repos/PythonApplication2/chromedriver_win32/chromedriver')


driver.get('https://movie.naver.com/movie/sdb/rank/rmovie.nhn')

soup = BeautifulSoup(driver.page_source,'lxml')

print(soup.prettify())

all_divs = soup.find_all('div',attrs={'class':'tit3'})

products = [div.div.a.span.string for div in all_divs]

for product in products:
    print(product)

driver.close()

