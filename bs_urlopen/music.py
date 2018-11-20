# https://www.crummy.com/software/BeautifulSoup/
from bs4 import BeautifulSoup
from urllib.request import urlopen
# lxml(4.2.5) 패키지 설치 필요
url = urlopen('https://music.bugs.co.kr/chart/track/realtime/total?chartdate=20181114')
soup = BeautifulSoup(url, 'lxml')
cnt_artist = 0
ctn_title = 0
 

for link1 in soup.find_all(name="p",attrs=({"class":"artist"})):
    cnt_artist += 1
    print(str(cnt_artist)+"위")
    print("아티스트 : "+link1.find('a').text)
    
print("-------------------------")
 
for link2 in soup.find_all(name="p",attrs=({"class":"title"})):
    ctn_title += 1
    print(str(ctn_title)+"위")
    print("노래제목"+link2.text)

