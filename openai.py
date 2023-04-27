import chromedriver_autoinstaller
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import os
import time

chromedriver_autoinstaller.install()

driver = webdriver.Chrome()
driver.get("https://openai.com/blog/chatgpt")
driver.implicitly_wait(3)

try_button = driver.find_element(by=By.CLASS_NAME, value="mr-gutter")
try_button.click()

driver.implicitly_wait(7)

# human=driver.find_element(by=By.CLASS_NAME, value="mark")
# driver.find_element_by_css_selector("input[type='checkbox']").click()
human = driver.find_element(by=By.CSS_SELECTOR, value="input[type='checkbox']")

driver.implicitly_wait(7)
human.click()

time.sleep(50)
driver.quit()
