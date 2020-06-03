import csv
import datetime
import re
import pandas as pd
import numpy as np
import matplotlib
import matplotlib.pyplot as plt


model_df = pd.read_csv("results.csv")
params_df= pd.read_csv("parametersR0.csv")
infection_df = model_df[['Infected','Run']]
infection_df = infection_df.apply(pd.to_numeric, errors='coerce')
max_infected_perRun = infection_df.groupby('Run')['Infected'].max()

#infection_df.groupby('Run')['Infected'].max().plot.box()
#infection_df.groupby('Run')['Infected'].max().plot.hist(bins=30)
#infection_df.groupby('Run')['Infected'].max().plot.hist(bins=30)

#time_series_df = model_df[['Infected','Run','Time']]
#first_chunk = time_series_df.iloc[:600]
#first_chunk['Time'] = pd.to_datetime(first_chunk['Time'])
first_chunk = pd.DataFrame(first_chunk['Infected'],columns=first_chunk['Run'])
#first_chunk.plot()
#time_series_df.plot()


infection_df.groupby('Run')['Infected'].max().plot.box()
#print(infection_df.groupby('Run')['Infected'].max())
plt.show()
