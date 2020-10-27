from selenium import webdriver
import time

def get_replys(url, inp_time=5, delay_time=0.3):
    #url = 'https://news.naver.com/main/read.nhn?m_view=1&mode=LSD&mid=shm&sid1=100&oid=437&aid=0000250784'

    # 웹 드라이버
    driver = webdriver.Chrome('./chromedriver.exe')
    driver.implicitly_wait(inp_time)
    driver.get(url)

    # 더보기 계속 클릭
    while True:
        try:
            #more = driver.find_element_by_css_selector('span.u_cbox_in_view_comment')
            #more.click()
            #time.sleep(1)
            more2 = driver.find_element_by_css_selector('a.u_cbox_btn_more')
            more2.click()
            time.sleep(delay_time)
        except:
            break
    print("끝")

    # 댓글 추출
    contents = driver.find_elements_by_css_selector('span.u_cbox_contents')
    # for content in contents:
    #     print(content.text)
    contents = [content.text for content in contents]

    # 작성자 추출
    nicks = driver.find_elements_by_css_selector('span.u_cbox_nick')
    # for nick in nicks:
    #     print(nick.text)
    nicks = [nick.text for nick in nicks]

    # 날짜 추출
    dates = driver.find_elements_by_css_selector('span.u_cbox_date')
    # for date in dates:
    #     print(date.text)
    dates = [date.text for date in dates]

    # 데이터 취합
    replys = list(zip(nicks, dates, contents))
    # for reply in replys:
    #    print(reply)

    driver.quit()
    return replys

if __name__ == '__main__':
    from datetime import datetime
    start = datetime.now()

    url = 'https://news.naver.com/main/read.nhn?m_view=1&mode=LSD&mid=shm&sid1=100&oid=437&aid=0000250784'
    # print(get_replys(url))
    reply_data = get_replys(url)

    import pandas as pd # 엑셀로 저장
    col = ['작성자', '날짜', '내용']
    data_frame = pd.DataFrame(reply_data, columns = col)
    data_frame.to_excel('news.xlsx', sheet_name='기사명', startrow=0, header=True)

    end = datetime.now()
    print(end-start)