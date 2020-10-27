# BeautifulSoup로 네이버 웹툰 썸네일 다운
from bs4 import BeautifulSoup
from pprint import pprint
import requests, re # re는 특수문자 처리
import os
from urllib.request import urlretrieve

# 저장 폴더 생성
try:
    if not (os.path.isdir('image')):
        os.makedirs(os.path.join('image'))
except OSError as e:
    if e.errno != errno.EEXIST:
        print("폴더 생성 실패")
        exit()


# 웹 페이지 열고 소스코드를 읽어옴
html = requests.get('https://comic.naver.com/webtoon/weekday.nhn')
soup = BeautifulSoup(html.text, 'html.parser')
html.close()

# 요일별 웹툰영역 추출
data1_list = soup.findAll('div',{'class':'col_inner'})
# pprint(data1_list)

# 전체 웹툰 리스트
li_list = []
for data1 in data1_list:
    # 제목 썸네일 영역 추출
    li_list.extend(data1.findAll('li'))

# pprint(li_list)

# 각각 썸네일과 제목 추출
for li in li_list:
    img = li.find('img')
    title = img['title']
    img_src = img['src']
    title = re.sub('[^0-9a-zA-Zㄱ-힗]', '', title) # 해당 영역의 글자가 아닌것은 ''로 치환
    # print(title, img_src)
    urlretrieve(img_src, './image/'+ title + '.jpg') # 주소, 파일경로+파일명+확장자