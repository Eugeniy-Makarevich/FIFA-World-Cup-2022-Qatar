#import modules
from bs4 import BeautifulSoup
from selenium import webdriver
import time,pandas as pd,re

#driver initialization
driver = webdriver.Chrome()
time.sleep(5)

#get url list
base_url = 'https://www.fifa.com/fifaplus/en/tournaments/mens/worldcup/'\
       'qatar2022/scores-fixtures?'
driver.get(base_url)
time.sleep(5)
soup = BeautifulSoup(driver.page_source,'html5lib')
   
url_list = ['https://fifa.com'+url['href'] for url in 
            soup.find_all('a', href=True) if 
            re.search("fifaplus/en/match-centre/match/.*",url['href'])]

#make columns
team1 = []
team2 = []
possesion_team1 = []
possesion_team2 = []

#
url = url_list[0]

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
teams =soup.find_all('div',{'class':'match-stats-tab-component_teamName__'\
                            '2D9h9'})
team1.append(teams[0].string)
team2.append(teams[1].string)

#possesion
possesion_team1.append(soup.find_all('p',{'class':'ff-m-0 single-stat-'\
          'possession-component_numberPercentLeft__1zQaX'})[0].string)
possesion_team2.append(soup.find_all('p',{'ff-m-0 single-stat-possession-'\
          'component_numberPercentRight__3IfVg'})[0].string)
    
#goals
all = soup.find_all('p',{'class':'ff-m-0 ff-mr-20'})
for el in all: print(el.string)
