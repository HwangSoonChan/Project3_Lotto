from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
import random

#로또 당첨 번호
win_cnt = []
win_num = []
num_cnt = []

#웹을 새로 생성
driver = webdriver.Chrome(r'C:\Users\HSC\chromedriver.exe')
url = 'https://www.dhlottery.co.kr/gameResult.do?method=byWin'
driver.get(url)

#로또 마지막 회차
max_cnt = int(driver.find_element_by_css_selector('#dwrNoList option').text)
print(max_cnt)

for i in range(0, 46):
    num_cnt.append(0)

for count in range(850,max_cnt):
    #로또 회차를 나타내는 부분
    select = Select(driver.find_element_by_id('dwrNoList'))
    select.select_by_value(str(count))
    driver.find_element_by_css_selector('.btn_common.form.blu').send_keys(Keys.ENTER)

    #웹에 있는 데이터를 불러옴
    page = driver.page_source
    soup = BeautifulSoup(page, "html.parser")

    #로또 등수정보
    lotto_rank = soup.select('tbody>tr>td')
    lo_rnk = [rank.text for rank in lotto_rank]

    #1등 당첨 인원이 12명 이상일 때
    if int(lo_rnk[2]) >= 10 :

        #로또 번호정보
        lotto_num = soup.select('.num.win span')
        lo_num = [int(num.text) for num in lotto_num]
        print("{}회차 번호는 : ".format(count))
        print(lo_num)

        for i in range(len(lo_num)):
            prase_num = int(lo_num[i])
            num_cnt[prase_num] += 1

        win_cnt.append(count)
        win_num.append(lo_num)

driver.close()

print(win_cnt)
print(win_num)
print(num_cnt)
print(len(win_num))

luk_num = []
reco_num1 = []
for i in range(46):
    if num_cnt[i] >= 8:
        luk_num.append(i)

print(luk_num)



if len(luk_num) >= 8 :
    for i in range(5):
        reco_num2 = []

        while(len(reco_num2)<6):
            rnd = random.randint(0, len(luk_num) - 1)

            if luk_num[rnd] not in reco_num2:
                reco_num2.append(luk_num[rnd])

        reco_num1.append(reco_num2)

    print(reco_num1)
else:
    print("추천할 번호가 없습니다.")