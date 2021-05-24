# importing selenium
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

import os
import wget  # download utility

path_to_driver = 'chromedriver.exe'
driver = webdriver.Chrome(path_to_driver)
driver.get('https://www.instagram.com/?hl=en')
accept_cookies = WebDriverWait(driver, 10).until(ec.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Accept All')]"))).click()
username = WebDriverWait(driver, 10).until(ec.element_to_be_clickable((By.CSS_SELECTOR, "input[name='username']")))  # targeting username
password = WebDriverWait(driver, 10).until(ec.element_to_be_clickable((By.CSS_SELECTOR, "input[name='password']")))  # targeting password
login = 'your_login'
haslo = 'your_password'
username.send_keys(login)  # entering username
password.send_keys(haslo)  # entering password
log_in = WebDriverWait(driver, 10).until(ec.element_to_be_clickable((By.CSS_SELECTOR, "button[type='submit']"))).click()
dont_save_lg = WebDriverWait(driver, 10).until(ec.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Not Now')]"))).click()
not_now = WebDriverWait(driver, 10).until(ec.element_to_be_clickable((By.CSS_SELECTOR, "button[class='aOOlW   HoLwm ']"))).click()
# because my Instagram account switches languages 24/7 I decided to choose elements by their classnames

keyword = 'python'
driver.get(f'https://www.instagram.com/explore/tags/{keyword}')  # searching by hashtag
driver.execute_script("window.scrollTo(0,4000);")
images = driver.find_elements_by_tag_name('img')
images = [image.get_attribute('src') for image in images]  # getting links of images

path = os.getcwd()
path = os.path.join(path, keyword)
os.mkdir(path)  # making directory for images with 'python' tag

counter = 0
for image in images:
    save_as = os.path.join(path, keyword + str(counter) + '.jpg')
    wget.download(image, save_as)
    counter += 1

driver.quit()