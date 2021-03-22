import requests
import time
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys

#로또 당첨 번호
win_num = []

#웹을 새로 생성
driver = webdriver.Chrome(r'C:\Users\HSC\chromedriver.exe')
url = 'https://www.dhlottery.co.kr/gameResult.do?method=byWin'
driver.get(url)

#로또 마지막 회차
max_cnt = int(driver.find_element_by_css_selector('#dwrNoList option').text)
print(max_cnt)

for count in range(1,max_cnt-400):
    #로또 회차를 나타내는 부분
    select = Select(driver.find_element_by_id('dwrNoList'))
    select.select_by_value(str(count))
    driver.find_element_by_css_selector('.btn_common.form.blu').send_keys(Keys.ENTER)

    #웹에 있는 데이터를 불러옴
    page = driver.page_source
    soup = BeautifulSoup(page, "html.parser")


#    #로또 회차정보를 카운트
#    lotto_count = soup.select('#dwrNoList option[value]')
#    lo_cnt = [count.get('value') for count in lotto_count]
#    print(lo_cnt)

    #로또 등수정보
    lotto_rank = soup.select('tbody>tr>td')
    lo_rnk = [rank.text for rank in lotto_rank]

    #1등 당첨 인원이 12명 이상일 때
    if int(lo_rnk[2]) >= 12 :
        #로또 번호정보
        lotto_num = soup.select('.num.win span')
        lo_num = [num.text for num in lotto_num]
        print("{}회차 번호는 : ".format(count))
        print(lo_num)
        win_num.append(lo_num)
    time.sleep(0.5)

print(win_num)
print(len(win_num))

#for i in range(1,len(value)):
#    page = requests.get("https://search.naver.com/search.naver?sm=tab_drt&where=nexearch&query=%d"%(i)+"회로또")
#    soup = BeautifulSoup(page.text, "html.parser")
#    num = [items.text for items in soup.select('.num_box>span')]
#    num.remove('보너스번호')
#    print(num)