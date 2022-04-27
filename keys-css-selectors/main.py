import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys

os.environ['PATH'] += r"C:/SeleniumDrivers/"
driver = webdriver.Chrome(executable_path='C:/SeleniumDrivers/chromedriver.exe')

driver.get('https://demo.seleniumeasy.com/basic-first-form-demo.html')
driver.implicitly_wait(5)

try:
    no_button = driver.find_element(By.CLASS_NAME, 'at-cm-no-button')
    no_button.click()
except:
    print('No element found')

sum1 = driver.find_element(By.ID, 'sum1')
sum2 = driver.find_element(By.ID, 'sum2')

sum1.send_keys(Keys.NUMPAD1, Keys.NUMPAD5)
sum2.send_keys(15)

btn = driver.find_element_by_css_selector('button[onclick="return total()"]')
btn.click()

