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

def BuscarCatalogo():

    metadata_catalogos = []

    lista_url_catalogos = []
    
    lista_catalogos = driver.find_elements(By.XPATH, '//div[@class="grid-item"]//a[1]')
    time.sleep(2)


    for catalogo in lista_catalogos:
        
        lista_url_catalogos.append(catalogo.get_attribute("href"))


for url_catalogo in lista_url_catalogos:

    driver.get(url_catalogo)
    time.sleep(2)

    metadata_catalogo = driver.find_element(By.XPATH, '//div[starts-with(@class="metadata")]')

    try :
        btnMostrarMas = metadata_catalogo.find_element(By.XPATH, './/button[@class="more-link show"]')
        if btnMostrarMas:
            btnMostrarMas.click()
    except:
        print("No")



    titulo = metadata_catalogo.find_element(By.XPATH, './/h1[@id="moviesDetailsH1"]').text

    largoTitulo = len(titulo)

    titulo = titulo[4 : largoTitulo-7]

     
    duracion = metadata_catalogo.find_element(By.XPATH, '//*[@id="subview-container"]/starz-movie-details/div/div/section/div[1]/div[2]/section/ul/li[2]').text

    sinopsis = metadata_catalogo.find_element(By.XPATH, '//*[@id="subview-container"]/starz-movie-details/div/div/section/div[1]/div[2]/div[1]/p').text

        año = metadata_catalogo.find_element(By.XPATH, '//*[@id="subview-container"]/starz-movie-details/div/div/section/div[1]/div[2]/section/ul/li[4]').text

        metadata_completa = []

        metadata_completa.append(titulo)
        metadata_completa.append(sinopsis)
        metadata_completa.append(año)
        metadata_completa.append(duracion)
        metadata_completa.append(url_catalogo)

        metadata_catalogos.append(metadata_completa)

    return metadata_catalogos

driver.get(website)

driver.maximize_window()

time.sleep(2)

btnSeries = driver.find_element(By.XPATH, '//a[@routerlink="/series"]')
btnSeries.click()

time.sleep(1)

btnVerTodo = driver.find_element(By.XPATH, '//a[@class="view-all"]')
btnVerTodo.click()

df = pd.DataFrame(BuscarPeliculasSeries(), columns=["Titulo", "Sinopsis", "Año", "Duracion", "Url"])
print(df)    
    
df.to_csv("series_text.cvs", index=False)

driver.get(website)

btnPeliculas = driver.find_element(By.XPATH, '//a[@routerlink="/movies"]')
btnPeliculas.click()

btnVerTodo = driver.find_element(By.XPATH, '//a[@class="view-all"]')
btnVerTodo.click()

df = pd.DataFrame(BuscarPeliculasSeries(), columns=["Titulo", "Sinopsis", "Año", "Duracion", "Url"])
print(df)    
    
df.to_csv("peliculas_text.cvs", index=False)

driver.quit()