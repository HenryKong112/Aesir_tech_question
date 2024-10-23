import q1
import pandas as pd

"""
Question 4: 
Write a function that takes a player_id as input and 
returns the player's highest score and the level at which it was achieved.
"""

print()
print('--Q4--')

# Define a function that accepts a player_id as input
def HIGHEST_SCORE_LEVEL(player_id: int):
    # Filter records for the specified player_id from the dataframe in q1
    player_record = q1.df[q1.df['player_id'] == player_id]
    
    # Check if the player has any records
    if not player_record.empty:
        # Identify the record with the highest score for the player
        highest_score_record = player_record.loc[player_record['score'].idxmax()]
        
        # Create a DataFrame with the player's highest score and the corresponding level
        result = pd.DataFrame({
            'Score': [highest_score_record['score']],
            'Level': [highest_score_record['level']]
        })
        
        # Print the result with a message for the specific player
        print(f"Player {player_id}'s highest score and the level at which it was achieved")
        print(result)
    else:
        # Print a message if the player_id is not found in the records
        print(f"Cannot find player_id {player_id}.")

# Example usage: Call the function with a specific player_id
HIGHEST_SCORE_LEVEL(104)

