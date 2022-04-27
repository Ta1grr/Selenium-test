import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

os.environ['PATH'] += r"C:/SeleniumDrivers/"
driver = webdriver.Chrome(executable_path='C:/SeleniumDrivers/chromedriver.exe')
driver.get('https://demo.seleniumeasy.com/jquery-download-progress-bar-demo.html')
driver.implicitly_wait(30)
my_element = driver.find_element(By.ID, 'downloadButton')
my_element.click()

progress_element = driver.find_element(By.CLASS_NAME, 'progress-label')
print(f"{progress_element.text == 'Completed!'}")

WebDriverWait(driver, 30).until(
    EC.text_to_be_present_in_element(
        (By.CLASS_NAME, 'progress-label'),
        'Completed!'
    )
)