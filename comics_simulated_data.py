##script to create random dataset with given variables

#load packages
import pandas as pd 
import numpy as np 

###PARAMETERS###
#48 total pairs seed 5 times each
pids = list(range(24))

#list columns
columns = ['condition','story','visual_clarity', 'visual_creativity', 'narrative_clarity', 'narrative_creativity', 'overall']
conditions = ['w','c']

#list DVs
dvs = ['visual_clarity', 'visual_creativity', 'narrative_clarity', 'narrative_creativity', 'overall']

###MAKE THE RANDOM SAMPLE###

#number of story prompts
stories = [1,2,3]
#each time each pair is seen
nset = [1,2,3,4,5]

#assign either a 0 for if control is chosen and 1 for if wizard is chosen
choices = [0,1]
#make the empty dataframe w/ participants and DVs as columns
df = pd.DataFrame(index=pids, columns=columns)

#divide data into half for each condition
df['condition'] = np.random.choice(conditions, size=len(df), p=[.50,.50])
#give each row a story prompt
df['story'] = np.random.choice(stories, size=len(df), p=[.33,.33,.34])


#randomize how many times a comic is chosen up to 5 times each
for dv in dvs:
	df[dv] = np.random.randint(0,6, size=(24,1))

print(df.head)

#export dataframe to csv
df.to_csv('comic_sim_data2.csv')

