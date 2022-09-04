import pandas as pd
import datetime as dt
import uuid 
import numpy as np

# Load in the data file
df = pd.read_csv('r/Users/thierrypierre/Downloads/School_Learning_Modalities.csv')

df 

countRows, countColumns = df.shape
