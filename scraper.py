#import modules
from bs4 import BeautifulSoup
from selenium import webdriver
import time
import pandas

#driver initialization
driver = webdriver.Chrome()
time.sleep(5)

#make columns
team1 = []
team2 = []

#make urls
url = 'https://www.fifa.com/fifaplus/en/match-centre/match/17/255711/285063/400235458'

#get url
driver.get(url)
time.sleep(5)

#find STATS button and click it
s = driver.find_element('xpath',"//*[contains(text(), 'STATS')]")
driver.execute_script("arguments[0].click();",s)
time.sleep(1)

#make a soup
soup = BeautifulSoup(driver.page_source,'html5lib')

#get values
#teams:
teams =soup.find_all('div',{'class':'match-stats-tab-component_teamName__2D9h9'})
team1.append(teams[0].string)
team2.append(teams[1].string)


