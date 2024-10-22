import q1
import pandas as pd

"""
Question 4: 
Write a function that takes a player_id as input and 
returns the player's highest score and the level at which it was achieved.

"""


print()
print('--Q4--')

def HIGHEST_SCORE_LEVEL(player_id):
    # Filter records for the specified player_id
    player_record = q1.df[q1.df['player_id'] == player_id]
    
    if not player_record.empty:
        # Find the record with the highest score
        highest_score_record = player_record.loc[player_record['score'].idxmax()]
        
        result = pd.DataFrame({
            'Score':[highest_score_record['score']],
            'Level':[highest_score_record['level']]
        })
        
        print(f"Player {player_id}'s highest score and the level at which it was achieved")
        print(result)
    else:
        print(f"Cannot find player_id {player_id}.")

# Example usage
HIGHEST_SCORE_LEVEL(104)
