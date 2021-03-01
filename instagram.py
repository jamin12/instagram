import requests
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

    broswer = webdriver.Chrome(options=options)
    broswer.maximize_window()
    #브라우저 연결
    broswer.get(url)
    return broswer

interval = 2

broswer = into_selenium("https://www.instagram.com/")
#wait 객체 생성
wait = WebDriverWait(broswer, 7)

#아이디 패스워드 입력 및 로그인
wait.until(EC.presence_of_element_located((By.XPATH,'//*[@id="loginForm"]/div/div[1]/div/label/input'))).send_keys("01074540118")
broswer.find_element_by_xpath('//*[@id="loginForm"]/div/div[2]/div/label/input').send_keys("[wzqxec951]")
broswer.find_element_by_xpath('//*[@id="loginForm"]/div/div[3]/button').click()

# 나의 프로필 접속
wait.until(EC.presence_of_element_located((By.XPATH,'//*[@id="react-root"]/section/main/div/div/div/div/button'))).click()
wait.until(EC.presence_of_element_located((By.XPATH,'/html/body/div[4]/div/div/div/div[3]/button[2]'))).click()
wait.until(EC.presence_of_element_located((By.XPATH,'//*[@id="react-root"]/section/main/section/div[3]/div[1]/div/div/div[1]/div/a'))).click()
#팔로워 확인
wait.until(EC.presence_of_element_located((By.XPATH,'//*[@id="react-root"]/section/main/div/header/section/ul/li[2]/a'))).click()

liElement = wait.until(EC.presence_of_element_located((By.XPATH,'/html/body/div[5]/div')))
broswer.execute_script("arguments[0].scrollIntoView(true);", liElement)

time.sleep(10)