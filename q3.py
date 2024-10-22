import q1
import matplotlib.pyplot as plt
import numpy as np

"""
Question 3: Data Visualization 
- Create a bar chart that shows the average score for each level.
- Create a pie chart that displays the distribution of score categories ('Low', 'Medium', 'High').
"""

# Filter out levels with zero average score
filtered_df = q1.df_avg[q1.df_avg['average_score'] > 0]  # Keep only levels with an average score greater than 0

even_x_values = np.arange(len(filtered_df))  # Create evenly spaced x-axis values based on the number of levels

# Create a bar chart for levels with non-zero average scores
plt.bar(even_x_values, filtered_df['average_score'])  # Plot the bar chart with x-values and the corresponding average scores

# Add labels and title to the bar chart
plt.xlabel('Level')  # Label for the x-axis (Level)
plt.ylabel('Average Score')  # Label for the y-axis (Average Score)
plt.title('Average Score by Level')  # Title for the bar chart

# Set the ticks on x-axis to only show levels with values
plt.xticks(even_x_values, filtered_df['level'])  # Replace numeric x-axis ticks with level labels from the filtered data

# Show the bar chart
plt.show()  # Display the bar chart

# Count the occurrences of each score category
category_count = q1.df['score_category'].value_counts()  # Count the number of occurrences for each score category (Low, Medium, High)

# Create a pie chart to show the distribution of players across score categories
plt.pie(category_count, autopct='%1.1f%%', startangle=90)  # Plot a pie chart, displaying percentages and starting at 90 degrees

# Add a legend to the pie chart
plt.legend(category_count.index, title="Score Category", bbox_to_anchor=(1, 1))  # Add a legend to the right of the chart, showing score categories

# Add a title to the pie chart
plt.title('Distribution of Players by Score Category')  # Title for the pie chart

# Show the pie chart
plt.show()  # Display the pie chart


