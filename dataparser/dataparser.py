import csv
import datetime
import re
import pandas as pd
import numpy as np
import matplotlib
import matplotlib.pyplot as plt

# Read in results and parameters for all varied parameters as dataframes
model_df = pd.read_csv("resultsR0Decay.csv")
params_df= pd.read_csv("parametersR0Decay.csv")
infection_df = model_df[['Infected','Run']]
infection_df = infection_df.apply(pd.to_numeric, errors='coerce')
max_infected_perRun = infection_df.groupby('Run')['Infected'].max()

#boxplot of max from each run
infection_df.groupby('Run')['Infected'].max().plot.box()
plt.show()

#histogram of max from each run
infection_df.groupby('Run')['Infected'].max().plot.hist(bins=30)
plt.show()



#Analyzing R0 Only

#read in data and crate dataframes
modelR0Only_df = pd.read_csv("resultsR0Only.csv")
paramsR0Only_df= pd.read_csv("parametersR0Only.csv")
infectionR0Only_df = modelR0Only_df[['Infected','Time','Run']]

#convert time to date
infectionR0Only_df['Time'] = infectionR0Only_df['Time'].apply(lambda x: str(x).split(' ')[0])
pd.to_datetime(infectionR0Only_df['Time'], format ='%Y-%m-%d')
#print(infectionR0Only_df.head)
#print(infectionR0Only_df.groupby('Run').groups)

#Tried to get R0 values into dataframe
# combined_df = infectionR0Only_df.join(paramsR0Only_df.set_index('Run'))
# combined_df = combined_df[['Infected','Time','Run', 'R0']]
# print(combined_df)
# R0Decays = []
# for i in range(0,51):
#     file = open('../v3/R'+str(i)+".txt", 'r')
#     R0Decays.append(file.read().replace('\n',' '))
# print(R0Decays)


#Plot time series of each run
infectionR0Only_df.pivot_table(index='Time',columns='Run',values='Infected').plot()
#print(infectionR0Only_df.pivot_table(index='Time',columns='Run',values='Infected'))
#infectionR0Only_df.plot()
plt.show()

#Show second half of runs
last_third_df = infectionR0Only_df.iloc[10000:,:]
last_third_df.pivot_table(index='Time',columns='Run',values='Infected').plot()
plt.show()


#Show current time onwards only
outlierGone_df = infectionR0Only_df.iloc[962:, :] #remove first  runs run becuase outlier

#first half of currently relevant runs
first_half= outlierGone_df.iloc[1:8000,:]
pivoted_df1 = first_half.pivot_table(index='Time',columns='Run',values='Infected')
first_current_df= pivoted_df1.iloc[200:,:]
first_current_df.plot()
plt.show()

#second half of currently relevant runs
second_half= outlierGone_df.iloc[8000:,:]
pivoted_df2 = second_half.pivot_table(index='Time',columns='Run',values='Infected')
second_half_current_df= pivoted_df2.iloc[200:,:]
second_half_current_df.plot()
plt.show()


