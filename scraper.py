#import modules
from bs4 import BeautifulSoup
from selenium import webdriver
import time,re,pandas as pd

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


#import dataframe pattern 
df = pd.read_csv('empty_df.csv',index_col = 0)

#main loop
for i,url in enumerate(url_list):

    #get url
    driver.get(url)
    time.sleep(8)

    #get OVERVIEW tab content
    s = driver.find_element('xpath',"//*[contains(text(), 'OVERVIEW')]")
    driver.execute_script("arguments[0].click();",s)
    time.sleep(2)
    soup = BeautifulSoup(driver.page_source,'html5lib')

    #get items from OVERVIEW tab
    overview = soup.find_all('div',
                    {'class':'match-details-overview-info_info__2LEuH'})
    df['date'][i] = overview[1].text.split(',')[0]
    df['time'][i] = overview[1].text.split(',')[1]
    df['city'][i] = overview[3].text
    df['stadium'][i] = overview[2].text
    df['referee'][i] = overview[4].text
    df['attendance'][i] = overview[8].text

    #get STATS tab content
    s = driver.find_element('xpath',"//*[contains(text(), 'STATS')]")
    driver.execute_script("arguments[0].click();",s)
    time.sleep(2)
    soup = BeautifulSoup(driver.page_source,'html5lib')

    #get items from STATS tab
    #teams:
    teams =soup.find_all('div',{'class':'match-stats-tab-component_teamName__'\
                            '2D9h9'})
    df['team1'][i] = teams[0].text
    df['team2'][i] = teams[1].text
    #possesion
    df['possesion_team1'][i] = soup.find_all('p',{'class':'ff-m-0 single-stat-'\
              'possession-component_numberPercentLeft__1zQaX'})[0].text
    df['possesion_team2'][i] = soup.find_all('p',{'ff-m-0 single-stat-possession-'\
              'component_numberPercentRight__3IfVg'})[0].text
    #other    
    df_columns_team1 =[value for value in df.columns.values
                       if re.findall('.*team1',value)]
    df_columns_team2 =[value for value in df.columns.values
                       if re.findall('.*team2',value)]
    
    team1_vals = soup.find_all('p',{'class':'ff-m-0 ff-mr-20'})
    for j,val in enumerate(df_columns_team1[2:]):
        df[val][i]=team1_vals[j].text
    
    team2_vals = soup.find_all('p',{'class':'ff-m-0 ff-ml-20'})
    for j,val in enumerate(df_columns_team2[2:]):
        df[val][i]=team2_vals[j].text
        
df.to_csv('FIFA WORLD CUP QATAR 2022.csv')