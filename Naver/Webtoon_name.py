# BeautifulSoup로 네이버웹툰 이름 크롤링
from bs4 import  BeautifulSoup
from pprint import pprint
import requests

html = requests.get('https://comic.naver.com/webtoon/weekday.nhn')
soup = BeautifulSoup(html.text, 'html.parser')
html.close()
# 월요 웹툰영역 추출
# data1 = soup.find('div',{'class':'col_inner'})
# pprint(data1)

# 모든 요일 웹툰영역 추출
data1_list = soup.findAll('div', {'class':'col_inner'})
pprint(data1_list)

# 모든 요일 제목
for data1 in data1_list:
    # 제목 포함 영역
    data2 = data1.findAll('a',{'class':'title'})
    #텍스트만 추출
    title_list = [t.text for t in data2]
    pprint(title_list)

# 제목 포함영역 추출
# data2 = data1.findAll('a', {'class':'title'})
# pprint(data2)

# 텍스트만 추출
# title_list = []
# for t in data2:
#    title_list.append(t.text)
# title_list = [t.text for t in data2] 와 동일
# pprint(title_list)