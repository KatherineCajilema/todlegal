import requests
from bs4 import BeautifulSoup as b
from selenium import webdriver
from selenium.common.exceptions import WebDriverException
import pandas as pd
from datetime import date 
import time 

#ubicacion = 'xxxxxx'
#driver=webdriver.Chrome(ubicacion)

url='https://dweet.io/follow/thecore'
#page=BeautifulSoup(driver.page_source,'html_parser')
html =requests.get(url)
content= html.content
soup=b(content,"lxml")
#print (soup)

#temperatura1 = soup.find('pre',{'id':'thing-data-raw'})
#print(temperatura1)
temperatura = soup.find("div", {"id" : "data-row-temperature"})

print(temperatura) 
#temperatura = soup.find("div",{class="dweet-data-value col-xs-8 text-right"}) 
