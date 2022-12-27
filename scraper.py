#import modules
from bs4 import BeautifulSoup
from selenium import webdriver
import time

#driver initialization
driver = webdriver.Chrome()
time.sleep(5)
url = 'https://www.fifa.com/fifaplus/en/match-centre/match/17/255711/285063/400235458'

#get url
driver.get(url)
time.sleep(5)

#find STATS button and click it
s = driver.find_element('xpath',"//*[contains(text(), 'STATS')]")
driver.execute_script("arguments[0].click();",s)

#make a soup
soup = BeautifulSoup(driver.page_source,'html5lib')


print(soup.find_all('p',{'class':'ff-m-0 ff-mb-8'}))
