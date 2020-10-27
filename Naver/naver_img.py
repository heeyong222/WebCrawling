# Selenium으로 네이버 사진 한번에 수집

from selenium import webdriver
import time, os
from selenium.webdriver.common.keys import Keys
from tqdm import tqdm
keyword = input("수집할 사진의 키워드를 입력하세요. :")

# web 접속 - 네이버 이미지 접속
print("접속중")
driver = webdriver.Chrome('./chromedriver.exe')
driver.implicitly_wait(30)


url = 'https://search.naver.com/search.naver?where=image&sm=tab_jum&query={}'.format(keyword)
driver.get(url)

# 페이지 스크롤다운
body = driver.find_element_by_css_selector('body')
for i in range(3):
    body.send_keys(Keys.PAGE_DOWN)
    time.sleep(1)


# 이미지 링크 수집
imgs = driver.find_elements_by_css_selector('img._img')
result = []
for img in tqdm(imgs):
    if 'http' in img.get_attribute('src'):
        result.append(img.get_attribute('src'))
print(result)

# driver.close()
print("수집 완료")

# 검색한 이름으로 폴더 생성

if not os.path.isdir('./{}'.format(keyword)):
    print("폴더 생성")
    os.mkdir('./{}'.format(keyword))

# 다운로드
from urllib.request import urlretrieve
# 확장자명 맞추기위해
for index, link in tqdm(enumerate(result)):
    start = link[0].rfind('.')
    end = link[0].rfind('&')
    filetype = link[start:end] #.png

    urlretrieve(link, './{}/{}{}{}'.format(keyword, keyword, index, filetype))
print("다운로드 완료")

# 압축하기
import zipfile
zip_file = zipfile.Zipfile('./{}.zip'.format(keyword), 'w')

for image in os.listdir('./{}'.format(keyword)):
    zip_file.write('./{}/{}'.format(keyword, image), compress_type=zipfile.ZIP_DEFLATED)
zip_file.close()
print("압축 완료")