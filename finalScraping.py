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

btn_peliculas = driver.find_element(By.XPATH, '//a[@routerlink="/movies"]')
btn_peliculas.click()

btn_ver_todo = driver.find_element(By.XPATH, '//a[@class="view-all"]')
btn_ver_todo.click()

time.sleep(2)

lista_peliculas = driver.find_elements(By.XPATH, '//div[@class="grid-item"]//a[1]')

time.sleep(2)

peliculas_metada = []

lista_url_peliculas = []

for pelicula in lista_peliculas:
    lista_url_peliculas.append(pelicula.get_attribute("href"))

n = 0

for url_peli in lista_url_peliculas:
    break
    n= n +1

    #if n >= 6:

    driver.get(url_peli)

    time.sleep(2)
    
    

    pelicula_metadata = driver.find_element(By.XPATH, '//div[starts-with(@class, "metadata")]')

    try :
        btn_mostrar_mas = pelicula_metadata.find_element(By.XPATH, './/button[starts-with(@class, "more-link show")]')
        if btn_mostrar_mas:
            btn_mostrar_mas.click()
    except:
        print("No")

    titulo = pelicula_metadata.find_element(By.XPATH, './/h1[@id="moviesDetailsH1"]').text

    largoTitulo = len(titulo)

    titulo = titulo[4 : largoTitulo-7]

    
    duracion = pelicula_metadata.find_element(By.XPATH, '//*[@id="subview-container"]/starz-movie-details/div/div/section/div[1]/div[2]/section/ul/li[2]').text

    sinopsis = pelicula_metadata.find_element(By.XPATH, '//*[@id="subview-container"]/starz-movie-details/div/div/section/div[1]/div[2]/div[1]/p').text

    año = pelicula_metadata.find_element(By.XPATH, '//*[@id="subview-container"]/starz-movie-details/div/div/section/div[1]/div[2]/section/ul/li[4]').text

    pelicula_metada = []

    pelicula_metada.append(titulo)
    pelicula_metada.append(sinopsis)
    pelicula_metada.append(año)
    pelicula_metada.append(duracion)
    pelicula_metada.append(url_peli)

    peliculas_metada.append(pelicula_metada)

df = pd.DataFrame(peliculas_metada, columns=["Titulo", "Sinopsis", "Año", "Duracion", "Url"])
print(df)    
    
df.to_csv("peliculas_text.cvs", index=False)

#Catalogo de Series

driver.get(website)

btn_series = driver.find_element(By.XPATH, '//a[@routerlink="/series"]')
btn_series.click()

time.sleep(1)

btn_ver_todo = driver.find_element(By.XPATH, '//a[@class="view-all"]')
btn_ver_todo.click()

lista_series = driver.find_elements(By.XPATH, '//div[@class="grid-item"]//a[1]')

time.sleep(2)

series_metadata = []

lista_url_series = []

for serie in lista_series:
    lista_url_series.append(serie.get_attribute("href"))

for url_serie in lista_url_series:

    driver.get(url_serie)

    time.sleep(2)

    serie_metadata = driver.find_element(By.XPATH, '//div[starts-with(@class, "metadata")]')

    try :
        btn_mostrar_mas = serie_metadata.find_element(By.XPATH, './/button[starts-with(@class, "more-link show")]')
        if btn_mostrar_mas:
            btn_mostrar_mas.click()
    except:
        print("No")

    titulo = serie_metadata.find_element(By.XPATH, './/h1[@id="moviesDetailsH1"]').text
    
    duracion = serie_metadata.find_element(By.XPATH, '/html/body/starz-root/div/div[1]/section/starz-series-details/div[1]/section/div[1]/div[2]/ul/li[2]').text

    sinopsis = serie_metadata.find_element(By.XPATH, './/p[@class="d-inline"]').text

    año = serie_metadata.find_element(By.XPATH, '//*[@id="subview-container"]/starz-series-details/div[1]/section/div[1]/div[2]/ul/li[4]').text

    metadata_completa = []

    metadata_completa.append(titulo)
    metadata_completa.append(sinopsis)
    metadata_completa.append(año)
    metadata_completa.append(duracion)
    metadata_completa.append(url_peli)

    series_metadata.append(metadata_completa)

df = pd.DataFrame(series_metadata, columns=["Titulo", "Sinopsis", "Año", "Duracion", "Url"])
print(df)    
    
df.to_csv("series_text.cvs", index=False)

driver.quit()