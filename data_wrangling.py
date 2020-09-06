import pandas as pd 
import numpy as np 
import csv

#read in data
data = pd.read_csv("data.csv")

dvs = ['visualClarityChoice','visualCreativityChoice','narrativeClarityChoice','narrativeCreativityChocie','overallChoice']


for i in data['visualClarityChoice']:
	data['vclarity'] = [1 if data]
	pd.np.where(data['visualClarityChoice'].str.contains("w"), 1)

print(data['vclarity'])