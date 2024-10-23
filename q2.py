import q1

"""
Question 2: Data Analysis 
- What is the average score of players across all levels?
- Which level has the highest average score?
- How many players scored in the 'High' category?
"""

print()
print("--Q2--")

# Calculate and print the average score of players across all levels
mean_score = q1.df_avg['average_score'].mean()  # Compute the mean of the 'average_score' column
print(f'Average score of players across all levels: {mean_score}')  # Display the calculated average score

# Identify and print the level with the highest average score
level_HAS = q1.df_avg.loc[q1.df_avg['average_score'].idxmax()]['level']  # Find the level corresponding to the highest average score
print(f'Level with the highest average score: {level_HAS}')  # Display the level with the highest average score

# Count and print the number of players who scored in the 'High' category
high_count = q1.df[q1.df['score_category'] == 'High'].shape[0]  # Count the number of rows where 'score_category' is 'High'
print(f"Number of players who scored in the 'High' category: {high_count}")  # Display the count of 'High' category players
