import time
from selenium import webdriver
from selenium.webdriver.edge.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

WEB_DRIVER = 'C:/Users/khem/Documents/edgedriver_win64'
USER_NAME = 'pybh_ai'
PASSWORD = 'khemkagame'
SIMIlLER_ACC = 'python.hub'


class InstaFollower:
    def __init__(self, web_driver):
        edge = web_driver
        opt = webdriver.EdgeOptions()
        opt.add_experimental_option('detach', True)
        self.driver = webdriver.Edge(options=opt, service=Service(executable_path=edge))

    def log_in(self):
        self.driver.get('https://www.instagram.com/')
        time.sleep(3)
        username = self.driver.find_element(By.XPATH, '//*[@id="loginForm"]/div/div[1]/div/label/input')
        username.send_keys(USER_NAME)

        password = self.driver.find_element(By.XPATH, '//*[@id="loginForm"]/div/div[2]/div/label/input')
        password.send_keys(PASSWORD, Keys.ENTER)

    def find_followers(self):
        time.sleep(3)
        search_icon = self.driver.find_element(By.XPATH,
                                               '/html/body/div[2]/div/div/div[2]/div/div/div/div[1]/div[1]/div[1]/div/div/div/div/div[2]/div[2]')
        search_icon.click()
        time.sleep(3)
        search = self.driver.find_element(By.CSS_SELECTOR, '._aauy')
        search.send_keys(SIMIlLER_ACC)
        time.sleep(3)
        search.send_keys(Keys.ENTER, Keys.ENTER)
        time.sleep(5)
        followers = self.driver.find_element(By.CSS_SELECTOR, '._alvs')
        followers.click()

        time.sleep(2)
        modal = self.driver.find_element(By.CSS_SELECTOR, '._aano')
        for i in range(10):
            self.driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", modal)
            time.sleep(2)

    def follow(self):
        time.sleep(5)
        follow_btn = self.driver.find_elements(By.CSS_SELECTOR, '.xamitd3 button')

        print(len(follow_btn))
        for i in follow_btn:
            i.click()
            time.sleep(1)

    # def follow(self):
    #     for i in range(100):


obj = InstaFollower(WEB_DRIVER)
obj.log_in()
time.sleep(5)
obj.find_followers()
obj.follow()
