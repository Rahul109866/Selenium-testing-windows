# requisites
from selenium import webdriver
import chromedriver_autoinstaller
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import os
import time

# chrome driver updater and path setting
chromedriver_autoinstaller.install()

# open Chrome and Navigate to LinkedIn Website
driver = webdriver.Chrome()  # open Chrome browser
driver.get("https://in.linkedin.com/")
driver.maximize_window()  # maximize the Chrome window
driver.implicitly_wait(4)  # give the browser time to load the page fully

# assigning the target fields to variables
username_field = driver.find_element(by=By.XPATH, value="//input[@id='session_key']")
password_field = driver.find_element(by=By.XPATH, value="//input[@id='session_password']")
# navigate and enter username
username_field.click()
username_field.send_keys("kumarkyle287@gmail.com")

# navigate and enter password
password_field.click()
password_field.send_keys("goodlord123")

# navigate to and click submit
submit_button = driver.find_element(by=By.XPATH,
                                    value="//*[@id='main-content']/section[1]/div/div/form[1]/div[2]/button")
submit_button.click()


# search=driver.find_element(by=By.XPATH, value="//input[@aria-label='search']")
search=driver.find_element(by=By.CLASS_NAME, value="search-global-typeahead__input")
search.send_keys("Wendy's")
search.send_keys(Keys.ENTER)

button_text = "Companies"
button = driver.find_element(By.XPATH, f"//button[text()='{button_text}']")
button.click()


search.click()
time.sleep(300)  # time the browser is opened. Have to mention explicitly due to automatic closing
driver.quit()  # close chrome

#test_for_branch