from selenium import webdriver      # imports
from time import sleep
from bs4 import BeautifulSoup


# make a webdriver object   -    chrome driver path for my system -- >    /Users/waqarjoyia/Downloads/chromedriver


driver = webdriver.Chrome('C:/Users/1027/source/repos/PythonApplication2/chromedriver_win32/chromedriver')

# open some page using get method       - url -- > parameters

driver.get('http://sh-shin.com/')

# driver.page_source

soup = BeautifulSoup(driver.page_source,'lxml')

print(soup.prettify())



# close webdriver object

driver.close()


