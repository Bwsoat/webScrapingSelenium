from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time

website= "https://www.netflix.com/ar/"


s = Service('./chromedriver')

driver = webdriver.Chrome(service=s)

driver.get(website)

headerTitle = driver.find_element(By.XPATH, '//*[@id="appMountPoint"]/div/div/div/div/div/div[1]/div/a')
iniciarSesion = driver.find_element(By.XPATH, '//*[@id="appMountPoint"]/div/div/div/div/div/div[1]/div/a')
time.sleep(5)
iniciarSesion.click()
print(headerTitle.text)

