
# country population
import pandas as pd     #install all in settings below
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

# create a driver instance (need to download and replace with your folder link)
driver = webdriver.Chrome("C://Users//shant//Downloads//chromedriver_win32//chromedriver.exe")
driver.get('https://www.worldometers.info/world-population/population-by-country/')
# get the html page
content = driver.page_source
html_page = driver.page_source
# create a soup object
soup = BeautifulSoup(driver.page_source, 'html.parser')
bold_style_1 = soup.find_all('td', attrs={'style': 'font-weight: bold; font-size:15px; text-align:left'})
bold_style_2 = soup.find_all('td', attrs={'style': 'font-weight: bold;'})
# Store the attributes into two lists
list1 = []
list2 = []
for item in bold_style_1:
    list1.append(item.text)
for item in bold_style_2:
    list2.append(item.text)
# Place lists into a csv file
df = pd.DataFrame({'Country':list2, 'Population':list1})
df.to_csv('Population.csv')
# close the driver
driver.close()