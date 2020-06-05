import csv
import datetime
import re
import pandas as pd
import numpy as np
import matplotlib
import matplotlib.pyplot as plt


# model_df = pd.read_csv("results.csv")
# params_df= pd.read_csv("parametersR0.csv")
# infection_df = model_df[['Infected','Run']]
# infection_df = infection_df.apply(pd.to_numeric, errors='coerce')
# max_infected_perRun = infection_df.groupby('Run')['Infected'].max()

#infection_df.groupby('Run')['Infected'].max().plot.box()
#infection_df.groupby('Run')['Infected'].max().plot.hist(bins=30)
#infection_df.groupby('Run')['Infected'].max().plot.hist(bins=30)

#time_series_df = model_df[['Infected','Run','Time']]
#first_chunk = time_series_df.iloc[:600]
#first_chunk['Time'] = pd.to_datetime(first_chunk['Time'])
# first_chunk = pd.DataFrame(first_chunk['Infected'],columns=first_chunk['Run'])
# #first_chunk.plot()
# #time_series_df.plot()


# infection_df.groupby('Run')['Infected'].max().plot.box()
# #print(infection_df.groupby('Run')['Infected'].max())
# plt.show()



#Analyzing R0 Only
modelR0Only_df = pd.read_csv("resultsR0Only.csv")
paramsR0Only_df= pd.read_csv("parametersR0Only.csv")
infectionR0Only_df = modelR0Only_df[['Infected','Time','Run']]

infectionR0Only_df['Time'] = infectionR0Only_df['Time'].apply(lambda x: str(x).split(' ')[0])
pd.to_datetime(infectionR0Only_df['Time'], format ='%Y-%m-%d')
##print(infectionR0Only_df.head)
#print(infectionR0Only_df.groupby('Run').groups) #= pd.DataFrame(infectionR0Only_df['Infected'],columns=infectionR0Only_df['Run'])columns=infectionR0Only_df.groupby('Run').groups


# timeseries_df =pd.DataFrame(infectionR0Only_df['Infected'], index= pd.date_range('2020-01-15', periods=300))
# print(timeseries_df)

combined_df = infectionR0Only_df.join(paramsR0Only_df.set_index('Run'))
print(combined_df)
worstR0Decays = []
for i in range(0,51):
    file = open('../v3/R'+str(i)+".txt", 'r')
    worstR0Decays.append(file.read().replace('\n',' '))


# infectionR0Only_df.pivot_table(index='Time',columns='Run',values='Infected').plot()
# print(infectionR0Only_df.pivot_table(index='Time',columns='Run',values='Infected'))
# #infectionR0Only_df.plot()
# plt.show()

