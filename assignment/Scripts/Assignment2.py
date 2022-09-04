import pandas as pd
import datetime as dt
import uuid 
import numpy as np

# Load in the data file
# df = pd.read_csv('/Users/thierrypierre/Downloads/hha-data-cleaning-main/Data/School_Learning_Modalities.csv')
df = pd.read_csv('assignment/raw/School_Learning_Modalities.csv')
print(df)
df 

# Prints the count of columns and rows 
countRows, countColumns = df.shape
