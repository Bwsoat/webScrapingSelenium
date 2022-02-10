from email.header import Header
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time
from selenium.webdriver.common.keys import Keys
import pandas as pd
from pymongo import MongoClient
import json


website= "https://www.starz.com/ar/es/"


s = Service('./chromedriver')

driver = webdriver.Chrome(service=s)

driver.get(website)

driver.maximize_window()

time.sleep(2)

import ipdb; ipdb.set_trace()


btnPeliculas = driver.find_element(By.XPATH, '//a[@routerlink="/movies"]')
btnPeliculas.click()

last_height = driver.execute_script("return document.body.scrollHeight")
SCROLL_PAUSE_TIME = 0.5

while False:
    # Scroll down to bottom
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    # Wait to load page
    time.sleep(SCROLL_PAUSE_TIME)

    # Calculate new scroll height and compare with last scroll height
    new_height = driver.execute_script("return document.body.scrollHeight")
    if new_height == last_height:
        break
    last_height = new_height

btnVerTodo = driver.find_element(By.XPATH, '//a[@class="view-all"]')
btnVerTodo.click()

time.sleep(2)

listaPeliculas = driver.find_elements(By.XPATH, '//div[@class="grid-item"]//a[1]')

time.sleep(2)

peliculasMetada = []

listaUrlPeliculas = []

for pelicula in listaPeliculas:
    listaUrlPeliculas.append(pelicula.get_attribute("href"))

for urlPeli in listaUrlPeliculas:

    driver.get(urlPeli)

    time.sleep(2)
    
    

    metaData = driver.find_element(By.XPATH, '//div[@class="metadata col-md-8"]')

    try :
        btnMostrarMas = metaData.find_element(By.XPATH, './/button[@class="more-link show"]')
        if btnMostrarMas:
            btnMostrarMas.click()
    except:
        print("No")

    titulo = metaData.find_element(By.XPATH, './/h1[@id="moviesDetailsH1"]').text

    largoTitulo = len(titulo)

    titulo = titulo[4 : largoTitulo-7]

    
    duracion = metaData.find_element(By.XPATH, '//*[@id="subview-container"]/starz-movie-details/div/div/section/div[1]/div[2]/section/ul/li[2]').text

    sinopsis = metaData.find_element(By.XPATH, '//*[@id="subview-container"]/starz-movie-details/div/div/section/div[1]/div[2]/div[1]/p').text

    año = metaData.find_element(By.XPATH, '//*[@id="subview-container"]/starz-movie-details/div/div/section/div[1]/div[2]/section/ul/li[4]').text

    peliculaMetada = []

    peliculaMetada.append(titulo)
    peliculaMetada.append(sinopsis)
    peliculaMetada.append(año)
    peliculaMetada.append(duracion)
    peliculaMetada.append(urlPeli)

    peliculasMetada.append(peliculaMetada)



    
df = pd.DataFrame(peliculasMetada, columns=["Titulo", "Sinopsis", "Año", "Duracion", "Url"])
print(df)    
    

df.to_csv("Peliculas_text.cvs", index=False)

#def mongoimport(csv_path, web_scraping_selenium, desarrollo_web, db_url='localhost', db_port=27000)
#    """ Imports a csv file at path csv_name to a mongo colection
#    returns: count of the documants in the new collection
#    """
#    client = MongoClient(db_url, db_port)
#    db = client[db_name]

driver.quit()

