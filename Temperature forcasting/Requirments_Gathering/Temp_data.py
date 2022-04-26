# -*- coding: utf-8 -*-
"""
Created on Fri Apr 15 19:42:02 2022

@author: rkvarma4518
"""


"""
January
February
March
April
May
june
july
August
September
October
November
December
"""



from bs4 import BeautifulSoup
from requests_html import HTMLSession

s= HTMLSession()

month = input("Enter month : ")
year = int(input("Enter year : "))

url = f'https://www.accuweather.com/en/in/satara/189287/{month}-weather/189287?year={year}'

r = s.get(url).text

#code = r.read()
soup = BeautifulSoup(r,'lxml')
#print(soup)

#Data present in whole page
All_data = soup.find('div', class_ = 'monthly-calendar')
date = All_data.find_all('div', class_ = 'date')


Date_list = []
for item in date:
    text = item.text.replace('\n','')
    text2 = text.replace('\t','')
    Date_list.append(text2)
#print(Date_list)


#High Temperature
hightemp = All_data.find_all('div', class_ = 'high')

hightemp_list = []
for item in hightemp:
    text = item.text.replace('\n','')
    text2 = text.replace('\t','')
    hightemp_list.append(text2)
#print(hightemp_list)


#Lowtemperature
lowtemp = All_data.find_all('div', class_ = 'low')

lowtemp_list = []
for item in lowtemp:
    text = item.text.replace('\n','')
    text2 = text.replace('\t','')
    lowtemp_list.append(text2)
#print(lowtemp_list)

res_dct = list(zip(Date_list,hightemp_list,lowtemp_list))
#print(res_dct)
#print(res_dct[1])

#Converting all Data in Table format.
import pandas as pd
df = pd.DataFrame(res_dct)
#print(df.head())
df.to_csv(f"{month}{year}.csv")
print("Data saved in Directory in CSV format")