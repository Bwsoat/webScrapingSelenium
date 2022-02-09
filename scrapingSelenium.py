from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time
from selenium.webdriver.common.keys import Keys

website= "https://www.starz.com/ar/es/"


s = Service('./chromedriver')

driver = webdriver.Chrome(service=s)

driver.get(website)

driver.maximize_window()

time.sleep(2)

#btnHamburger = driver.find_element(By.XPATH, '//*[@id="view-container"]/starz-header/header/div/div/div[4]/button')
#btnHamburger.click()

btnPeliculas = driver.find_element(By.XPATH, '//a[@routerlink="/movies"]')
btnPeliculas.click()

btnVerTodo = driver.find_element(By.XPATH, '//a[@class="view-all"]')
btnVerTodo.click()

time.sleep(2)

#btnVerTodo = driver.find_element(By.XPATH, '//*[@id="subview-container"]/starz-view-all/div/div/div/div/div/div/section/nav/ul/li[2]/span')
#btnVerTodo.click()
#html = driver.find_element(By.TAG_NAME, 'html')

listaPeliculas = driver.find_elements(By.XPATH, '//div[@class="view-all-link"]')
#print(listaPeliculas.text)
time.sleep(2)

for pelicula in listaPeliculas:
    import ipdb; ipdb.set_trace()
    time.sleep(5)

    pelicula.click()

    #masInfo = pelicula.find_element(By.XPATH, './/article[@class="content-link"]')
    #masInfo.find_element(By.XPATH, './/a[1]').click()
    
    time.sleep(2)
    metaData = driver.find_element(By.CLASS_NAME, 'metadata')
    print(metaData.text)

    time.sleep(2)

    driver.back()


driver.quit()

