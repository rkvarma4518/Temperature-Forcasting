# -*- coding: utf-8 -*-
"""
Created on Sun Apr 24 14:38:17 2022

@author: DELL
"""


import numpy as np
import pandas as pd

df = pd.read_csv("C:/Users/DELL/Desktop/data/Dataset.csv")

#print(df.head())
#print(df['high'])



# preparing independent and dependent features
def prepare_data(timeseries_data, n_features):
	X, y =[],[]
	for i in range(len(timeseries_data)):
		# find the end of this pattern
		end_ix = i + n_features
		# check if we are beyond the sequence
		if end_ix > len(timeseries_data)-1:
			break
		# gather input and output parts of the pattern
		seq_x, seq_y = timeseries_data[i:end_ix], timeseries_data[end_ix]
		X.append(seq_x)
		y.append(seq_y)
	return np.array(X), np.array(y)

high_data = df['high']
# choose a number of time steps
n_steps = 3
# split into samples
X, y = prepare_data(high_data, n_steps)

low_data = df['low']
n_steps = 3
X2, y2 = prepare_data(low_data, n_steps)


#print(X)
#print(y)
#print(X2)
#print(y2)


X = pd.DataFrame(X)
X.to_csv('X.csv', index=False)
y = pd.DataFrame(y)
y.to_csv('y.csv', index=False)
X2 = pd.DataFrame(X2)
X2.to_csv('X2.csv', index=False)
y2 = pd.DataFrame(y2)
y2.to_csv('y2.csv', index=False)