import q1
import matplotlib.pyplot as plt
import numpy as np

"""
Question 3: Data Visualization 
- Create a bar chart that shows the average score for each level.
- Create a pie chart that displays the distribution of score categories ('Low', 'Medium', 'High').
"""

# Filter out levels with zero average score from the dataset
filtered_df = q1.df_avg[q1.df_avg['average_score'] > 0]  # Keep only levels where the average score is greater than 0

# Generate evenly spaced x-axis values based on the number of levels
even_x_values = np.arange(len(filtered_df))  # This will be used to position bars on the x-axis

# Create a bar chart to display the average score for each level with non-zero average scores
plt.bar(even_x_values, filtered_df['average_score'])  # Plot the average score for each level

# Add labels and a title to the bar chart
plt.xlabel('Level')  # Label for the x-axis (shows level numbers)
plt.ylabel('Average Score')  # Label for the y-axis (shows the average score for each level)
plt.title('Average Score by Level')  # Add a title to the bar chart

# Replace the numeric x-axis tick labels with actual level numbers from the filtered data
plt.xticks(even_x_values, filtered_df['level'])  # Match x-axis values with level names or numbers

# Show the bar chart
plt.show()  # Display the bar chart visualization

# Count the occurrences of each score category ('Low', 'Medium', 'High') in the dataset
category_count = q1.df['score_category'].value_counts()  # Count the number of occurrences for each score category

# Create a pie chart to show the distribution of players across different score categories
plt.pie(category_count, autopct='%1.1f%%', startangle=90)  # Plot a pie chart, displaying percentages and starting at 90 degrees for clarity

# Add a legend to the pie chart, showing what each color represents
plt.legend(category_count.index, title="Score Category", bbox_to_anchor=(1, 1))  # Add a legend box to the right side of the chart

# Add a title to the pie chart
plt.title('Distribution of Players by Score Category')  # Title for the pie chart

# Show the pie chart
plt.show()  # Display the pie chart visualization



