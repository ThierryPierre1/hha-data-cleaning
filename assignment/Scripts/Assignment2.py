import pandas as pd
import datetime as dt
import uuid 
import numpy as np

# Load in the data file
# df = pd.read_csv('/Users/thierrypierre/Downloads/hha-data-cleaning-main/Data/School_Learning_Modalities.csv')
df = pd.read_csv('assignment/Data/School_Learning_Modalities.csv')
print(df)

# Print the count of columns and rows 
df.shape

# Provide a print out of the column names 
list(df)

# Clean the column names ## regex 
df.columns = df.columns.str.replace('[^A-Za-z0-9]+', '_') 
df.columns = df.columns.str.replace(' ', '_') 

# Clean the strings that might exist within each column
df.dtypes

#  Assess white space or special characters 
df.columns = df.columns.str.replace(' ', '_') 
list(df)

# Convert the column types to the correct types
df.sample
df ['Week'] = pd.to_datetime(df['Week'])

# Look for duplicate rows and remove duplicate rows 
df.drop_duplicates(subset=None, keep='first', inplace=False, ignore_index=False)

# Assess missingness (count of missing values per column) 
df.isnull().sum()

# New data

def A (Learning_Modality):
    if Learning_Modality== 'In_Person':
        return "True" 
    else:
        return "False"

df['modality_inperson'] = np.where(df["Learning_Modality"] == 'In Person', True, False)
df.dtypes

list(df)

df.to_csv('assignment/Data/School_Learning_Modalities.csv')
