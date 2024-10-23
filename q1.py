import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

"""
Question 1: Data Manipulation (30 points)
1. Load the CSV file 'gamdata.csv' containing the columns: 
   - game_id
   - player_id
   - score
   - level
   - timestamp
2. Perform the following operations:
   - Clean the data by removing rows with missing values.
   - Add a new column 'score_category' to classify scores into:
     - 'Low': score < 50
     - 'Medium': 50 <= score < 80
     - 'High': score >= 80
   - Group the data by 'level' and compute the average score for each level.
"""
print("--Q1--")
# Load the csv file into a DataFrame 
df = pd.read_csv('gamdata.csv',sep='|',usecols=[' game_id ',' player_id ',' score ',' level ',' timestamp '])

# Read from row 1 as row 0 is "----"
df = df.iloc[1:]

# Clean the data by removing any rows with missing values.
df = df.dropna()

# Clean the column names by removing leading and trailing spaces
df.columns = df.columns.str.strip()

# Clean the DataFrame values by removing leading and trailing spaces
df = df.applymap(lambda x: x.strip() if isinstance(x, str) else x)

# Check data types
print(df.info())

# change data type
df[['game_id','player_id','score','level']] = df[['game_id','player_id','score','level']].astype(int)
df['timestamp'] = df['timestamp'].astype('datetime64[ns]')

# Check data types again
print(df.info())

# Define cutoff points and labels for score categories
cutoff = [0, 50, 80, np.inf]
label = ["Low", "Medium", "High"]

# Create a new column 'score_category'
df["score_category"] = pd.cut(df["score"], bins=cutoff, labels=label, right=False)
print(df)

# Group the data by 'level' and calculate the average score for each level.
df_avg = df.groupby('level')['score'].agg('mean').reset_index()
df_avg.columns = ['level', 'average_score']
print(df_avg)






