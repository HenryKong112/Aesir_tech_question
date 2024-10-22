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
mean_score = q1.df_avg['average_score'].mean()
print(f'Average score of players across all levels: {mean_score}')

# Identify and print the level with the highest average score
level_HAS = q1.df_avg.loc[q1.df_avg['average_score'].idxmax()]['level']
print(f'Level with the highest average score: {level_HAS}')

# Count and print the number of players who scored in the 'High' category
high_count = q1.df[q1.df['score_category'] == 'High'].shape[0]
print(f"Number of players who scored in the 'High' category: {high_count}")