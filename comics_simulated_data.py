##script to create random dataset with given variables

#load packages
import pandas as pd 
import numpy as np 

###PARAMETERS###
#48 total pairs seed 5 times each
pids = list(range(240))

#list columns
columns = ['story','set','visual_clarity', 'visual_creativity', 'narrative_clarity', 'narrative_creativity', 'overall']

###MAKE THE RANDOM SAMPLE###

#number of story prompts
stories = [1,2,3]
#each time each pair is seen
nset = [1,2,3,4,5]

#assign either a 0 for if control is chosen and 1 for if wizard is chosen
choices = [0,1]
#make the empty dataframe w/ participants and DVs as columns
df = pd.DataFrame(index=pids, columns=columns)

#give each row a story prompt
df['story'] = np.random.choice(stories, size=len(df), p=[.33,.33,.34])

#each pair in each story is seen 5 times
for story in stories:
	df['set'] = np.random.choice(nset, size=len(df), p=[.20,.20,.20,.20,.20])

#randomize DVs into condition
# for dv in dvs:
# 	df[dv] = np.random.choice(choices, size=len(df), p=[.30,.70])

#randomly assign either 1 or 0 for each DV 
df['visual_clarity'] = np.random.randint(0,2, size=(240,1))
df['visual_creativity'] = np.random.randint(0,2, size=(240,1))
df['narrative_clarity'] = np.random.randint(0,2, size=(240,1))
df['narrative_creativity'] = np.random.randint(0,2, size=(240,1))
df['overall'] = np.random.randint(0,2, size=(240,1))

print(df)

#export dataframe to csv
df.to_csv('comic_sim_data.csv')

