from selenium import webdriver
from bs4 import BeautifulSoup
 
driver = webdriver.Chrome("C:/Users/1027/source/repos/PythonApplication2/chromedriver_win32/chromedriver") # chromedriver 경로 설정
driver.implicitly_wait(3)
driver.get('https://nid.naver.com/nidlogin.login')
# 아이디/비밀번호를 입력해준다.
driver.find_element_by_name('id').send_keys('coolbeat')
driver.find_element_by_name('pw').send_keys('ilovejav@8')
driver.implicitly_wait(3)
 
driver.find_element_by_xpath('//*[@id="frmNIDLogin"]/fieldset/input').click()
driver.implicitly_wait(3)
 
driver.get('https://order.pay.naver.com/home')
html = driver.page_source
soup = BeautifulSoup(html, 'html.parser')
notices = soup.select('div.p_inr > div.p_info > a > span')
 
for n in notices:
    print(n.text.strip())
