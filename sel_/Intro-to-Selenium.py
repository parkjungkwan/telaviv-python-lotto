from selenium import webdriver      # imports
from time import sleep
from bs4 import BeautifulSoup


# make a webdriver object   -    chrome driver path for my system -- >    /Users/waqarjoyia/Downloads/chromedriver


driver = webdriver.Chrome('C:/Users/1027/source/repos/PythonApplication2/chromedriver_win32/chromedriver')

# open some page using get method       - url -- > parameters

driver.get('https://movie.naver.com/movie/sdb/rank/rmovie.nhn')

# driver.page_source

soup = BeautifulSoup(driver.page_source,'lxml')

print(soup.prettify())

all_divs = soup.find_all('div',attrs={'class':'tit3'})



products = [div.div.a.span.string for div in all_divs]

for product in products:
    print(product)

# close webdriver object

driver.close()

