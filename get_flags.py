#import modules
from bs4 import BeautifulSoup
from selenium import webdriver
import time,re,pandas as pd

#driver initialization
driver = webdriver.Chrome()
time.sleep(5)

#get url and make soup
url = 'https://www.fifa.com/fifaplus/en/tournaments/mens/worldcup/qatar2022/teams'
driver.get(url)
time.sleep(5)
soup = BeautifulSoup(driver.page_source,'html5lib')

#get country name and flag url
country_tags = soup.find_all('div',{'class':'flag-with-info_flagCountry__Yw8QR'})
country_list = [tag.text for tag in country_tags]
flag_tags = soup.find_all('img',src = True)
flag_list = [tag['src'] for tag in flag_tags 
             if re.findall('https://cloudinary.*',tag['src'])]
#export to file
df = pd.DataFrame({'country':country_list,'flag':flag_list})
df.to_csv('country_flags.csv',index=False)
