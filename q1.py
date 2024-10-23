import pandas as pd
import numpy as np

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

# Load the CSV file into a DataFrame, specifying the columns to load and separating values with '|'
df = pd.read_csv('gamdata.csv', sep='|', usecols=[' game_id ', ' player_id ', ' score ', ' level ', ' timestamp '])

# Remove the first row, assuming row 0 contains "----" or unwanted headers
df = df.iloc[1:]

# Clean the data by removing any rows that contain missing (NaN) values
df = df.dropna()

# Clean the column names by stripping leading and trailing spaces to ensure proper column access
df.columns = df.columns.str.strip()

# Apply a function to clean the DataFrame's string values by stripping leading and trailing spaces in the data itself
df = df.applymap(lambda x: x.strip() if isinstance(x, str) else x)

# Print data type information before data type conversion
print(df.info())

# Convert relevant columns to the correct data types: 'game_id', 'player_id', 'score', 'level' to integers, and 'timestamp' to datetime
df[['game_id', 'player_id', 'score', 'level']] = df[['game_id', 'player_id', 'score', 'level']].astype(int)
df['timestamp'] = df['timestamp'].astype('datetime64[ns]')

# Print data type information after the conversion to verify changes
print(df.info())

# Define cutoff points for categorizing scores into 'Low', 'Medium', and 'High' score categories
cutoff = [0, 50, 80, np.inf]  # Score ranges: 0 to <50 (Low), 50 to <80 (Medium), and 80 and above (High)
label = ["Low", "Medium", "High"]  # Labels corresponding to score ranges

# Create a new column 'score_category' that categorizes each player's score based on the defined bins
df["score_category"] = pd.cut(df["score"], bins=cutoff, labels=label, right=False)

# Print the DataFrame to check the new 'score_category' column
print(df)

# Group the data by 'level' and compute the average score for each level, returning a DataFrame with 'level' and 'average_score'
df_avg = df.groupby('level')['score'].agg('mean').reset_index()

# Rename the columns of the new DataFrame to 'level' and 'average_score'
df_avg.columns = ['level', 'average_score']

# Print the resulting DataFrame with the average score per level
print(df_avg)







