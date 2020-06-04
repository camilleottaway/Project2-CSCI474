import csv
import datetime
import re
import pandas as pd
import numpy as np
import matplotlib
import matplotlib.pyplot as plt


#model_df = pd.read_csv("resultsR0Decay.csv")
#model_df = pd.read_csv("resultsR0Only.csv")
model_df = pd.read_csv("resultsR0Decay.csv")
#params_df= pd.read_csv("parametersR0.csv")
#params_df= pd.read_csv("parametersR0Only.csv")
params_df= pd.read_csv("parametersR0Decay.csv")
params_df = params_df.apply(pd.to_numeric, errors='coerce')
infection_df = model_df[['Infected','Run']]
infection_df = infection_df.apply(pd.to_numeric, errors='coerce')
max_infected_perRun = infection_df.groupby('Run')['Infected'].max()
max_infected_perRun = max_infected_perRun.apply(pd.to_numeric, errors='coerce')

#infection_df.groupby('Run')['Infected'].max().plot.box()
#infection_df.groupby('Run')['Infected'].max().plot.hist(bins=30)

Q1=max_infected_perRun.quantile(0.25)
Q3=max_infected_perRun.quantile(0.75)
IQR = Q3 - Q1
max = Q3 + 1.5* IQR

biggest_infections = max_infected_perRun[max_infected_perRun.between(max, max_infected_perRun.quantile(0.99))]
biggest_infections = biggest_infections.to_frame()
worstR0 = biggest_infections.join(params_df.set_index('Run'))
R0_dups = worstR0['R0'].to_list()
R0s = []
for i in R0_dups:
    R0s.append(i)
    while i in R0_dups:
        R0_dups.remove(i)
#print(R0s)

worstR0Decays = []
for i in R0s:
    file = open('../v3/R'+str(i)+".txt", 'r')
    worstR0Decays.append(file.read().replace('\n',' '))

print("Social Distancing R0's for simulations above the 3rd quartile:")
print()
for i in worstR0Decays:
    print(i)

print()
print("Range of parameters for worst runs: ")
print("Infected: " + str(worstR0['Infected'].min()) + " - " + str(worstR0['Infected'].max()))
print("CFR: " + str(worstR0['CFR'].min()) + " - " +  str(worstR0['CFR'].max()))
print("dinf: " + str(worstR0['dinf'].min()) + " - " +  str(worstR0['dinf'].max()))
print("PSEVERE: " + str(worstR0['PSEVERE'].min()) + " - " +  str(worstR0['PSEVERE'].max()))
print("Number: " + str(worstR0['N'].min()) + " - " +  str(worstR0['N'].max()))



#max_infected_perRun.plot.box()
#plt.show()

#infection_df.groupby('Run')['Infected'].max().plot.box()
#print(max_infected_perRun.summary())
#print(infection_df.groupby('Run')['Infected'].max())
