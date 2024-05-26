from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from urllib.parse import quote_plus
import time

chrome_driver = (
    r"C:\Users\USER\Documents\GitHub\Web-Crawling\크롤링예제\driver\chromedriver.exe"
)


class User:
    def __init__(self):
        self.chrome_options = Options()
        # self.chrome_options.add_experimental_option("debuggerAddress", "127.0.0.1:9222")
        self.browser = webdriver.Chrome(options=self.chrome_options)
        # -------------------------------------------------------------------
        self.browser.maximize_window()

    def 페이지이동(self, page):
        self.browser.get(page)

    def 객체선택_값입력(self, user_xpath, item_name):
        self.browser.find_element(By.XPATH, user_xpath).send_keys(item_name)
        return self.browser

    def 객체선택_클릭(self, user_xpath):
        self.browser.find_element(By.XPATH, user_xpath).click()
        return self.browser

    def 객체선택_텍스트추출(self, user_xpath):
        self.browser.find_element(By.XPATH, user_xpath).text

    def 종료(self):
        self.browser.close()
        print("작업 완료됨")

    def 일반딜레이(self, second):
        time.sleep(second)

    def 브라우저딜레이(self, second=1):
        self.browser.implicitly_wait(second)

    def 새창으로활성이동(self, idx):
        # window_handles[0...]
        print(self.browser.window_handles)  # 0
        self.browser.switch_to.window(self.browser.window_handles[idx])

    def 마우스로이동하고클릭(self, user_xpath):
        ac = ActionChains(self.browser)
        web_elements = self.browser.find_element(By.XPATH, user_xpath)
        ac.click(web_elements)
        ac.perform
