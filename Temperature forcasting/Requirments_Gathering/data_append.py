# -*- coding: utf-8 -*-
"""
Created on Fri Apr 22 20:19:15 2022

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


import pandas as pd 

#input file name
filename1 = input("Please Enter File Name: ")


#reading csv file from directory
data = pd.read_csv("C:/Users/DELL\Desktop/data/Dataset.csv")
data2 = pd.read_csv(f"C:/Users/DELL\Desktop/data/{filename1}.csv")

#Create data into DataFrame
df1 = pd.DataFrame(data)
df2 = pd.DataFrame(data2)

#Concating both files 
All_data = pd.concat([df1,df2])
print(All_data)

#Convert data into csv
All_data.to_csv("Dataset.csv", index=False)