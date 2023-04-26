from selenium import webdriver
import chromedriver_autoinstaller
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import os
import time

chromedriver_autoinstaller.install()

driver = webdriver.Chrome()
driver.get("https://in.linkedin.com/")
driver.maximize_window()
driver.implicitly_wait(4)  # give the browser time to load the page fully

username_field = driver.find_element(by=By.XPATH, value="//input[@id='session_key']")
password_field = driver.find_element(by=By.XPATH, value="//input[@id='session_password']")
username_field.click()

username_field.send_keys("rahulrajendran1098@gmail.com")

password_field.click()

password_field.send_keys("faker.lol098")

submit_button = driver.find_element(by=By.XPATH,
                                    value="//*[@id='main-content']/section[1]/div/div/form[1]/div[2]/button")

submit_button.click()

time.sleep(30)
driver.quit()
