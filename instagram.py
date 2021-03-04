from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# selenium으로 접속하는 방법
def into_selenium(url):
    #브라우져 옵션 설정
    # options = webdriver.ChromeOptions()
    #화면 안뜨게
    # options.headless = True
    options = Options()
    #유저 에이전트 설정
    options.add_argument("Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.190 Safari/537.36")
    options.set_headless(False)

    browser = webdriver.Chrome(options=options)
    browser.maximize_window()
    #브라우저 연결
    browser.get(url)
    return browser

interval = 2

browser = into_selenium("https://www.instagram.com/")
#wait 객체 생성
wait = WebDriverWait(browser, 7)

#아이디 패스워드 입력 및 로그인
wait.until(EC.presence_of_element_located((By.XPATH,'//*[@id="loginForm"]/div/div[1]/div/label/input'))).send_keys("01074540118")
browser.find_element_by_xpath('//*[@id="loginForm"]/div/div[2]/div/label/input').send_keys("[wzqxec951]")
browser.find_element_by_xpath('//*[@id="loginForm"]/div/div[3]/button').click()

# 나의 프로필 접속
wait.until(EC.presence_of_element_located((By.XPATH,'//*[@id="react-root"]/section/main/div/div/div/div/button'))).click()
wait.until(EC.presence_of_element_located((By.XPATH,'/html/body/div[4]/div/div/div/div[3]/button[2]'))).click()
wait.until(EC.presence_of_element_located((By.XPATH,'//*[@id="react-root"]/section/main/section/div[3]/div[1]/div/div/div[1]/div/a'))).click()

#팔로워 확인
wait.until(EC.presence_of_element_located((By.XPATH,'//*[@id="react-root"]/section/main/div/header/section/ul/li[2]/a'))).click()

#스크롤
wait.until(EC.presence_of_element_located((By.XPATH,'/html/body/div[5]/div/div/div[2]/ul/div')))
oldHeight = -1
newHeight = -2
while oldHeight != newHeight:
    oldHeight = newHeight
    newHeight = browser.execute_script("return document.querySelectorAll('.jSC57')[0].scrollHeight")
    browser.execute_script("document.querySelectorAll('.isgrP')[0].scrollTo(0,document.querySelectorAll('.jSC57')[0].scrollHeight)")
    time.sleep(0.5)

#팔로워 목록 가져오기
soup = BeautifulSoup(browser.page_source,"lxml")
follower = soup.find_all("div", attrs = {"class" : "wFPL8"})
follower_name = []
for i in follower:
    follower_name.append(i.get_text())

browser.find_element_by_xpath('/html/body/div[5]/div/div/div[1]/div/div[2]/button').click()

#팔로잉 확인
wait.until(EC.presence_of_element_located((By.XPATH,'//*[@id="react-root"]/section/main/div/header/section/ul/li[3]/a'))).click()

wait.until(EC.presence_of_element_located((By.XPATH,'/html/body/div[5]/div/div/div[2]/ul/div')))

oldHeight = -1
newHeight = -2
while oldHeight != newHeight:
    oldHeight = newHeight
    newHeight = browser.execute_script("return document.querySelectorAll('._6xe7A')[0].scrollHeight")
    browser.execute_script("document.querySelectorAll('.isgrP')[0].scrollTo(0,document.querySelectorAll('._6xe7A')[0].scrollHeight)")
    time.sleep(0.5)

#팔로워 목록 가져오기
soup = BeautifulSoup(browser.page_source,"lxml")
following = soup.find_all("div", attrs = {"class" : "wFPL8"})
following_name = []
for i in following:
    following_name.append(i.get_text())

#팔로우는 했지만 팔로워가 안된 사람들 추출
if len(follower_name) < len(following_name):
    for i in follower_name:
        if i in following_name:
            following_name.remove(i)
else:
    for i in following_name:
        if i in follower_name:
            follower_name.remove(i)

print(following_name)

time.sleep(3)

