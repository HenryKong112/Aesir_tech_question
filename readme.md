# Installation

1. Clone the repository:
```
git clone https://github.com/HenryKong112/Aesir_tech_question.git
```
```
cd Aesir_tech_question
```

2. Install required packages:

Python Version: Python 3.12.4

```
pip install -r requirement.txt
```

# Answer for question 1 to 4
## Question 1

```python
python q1.py
```



Group the data by 'level' and compute the average score for each level.



Explanation of the Code:
1. Data Loading: The code loads data from gamdata.csv, specifying the relevant columns.

2. Data Cleaning:
    - It removes rows with missing values.
    - Cleans column names and data entries by stripping whitespace.

3. Data Type Conversion: Converts relevant columns to appropriate data types.

4. Score Categorization: A new column score_category is created based on predefined score thresholds.

    <img src='image\q1_addcolumn.png'>

5. Average Score Calculation: Groups the data by level and computes the average score for each level.

    <img src='image\q1_GroupByLevel.png'>


## Question 2

```python
python q2.py
```

Explanation of the Code:

1. Average Score Calculation: The code calculates the average score of players across all levels using the mean() function on the average_score column.

2. Level with Highest Average Score: It identifies the level with the highest average score by finding the index of the maximum value in the average_score column.

3. Counting High Scorers: It counts how many players fall into the 'High' score category by filtering the DataFrame.

Result:

<img src='image\q2.png'>

## Question 3

```python
python q3.py
```

Explanation of the Code:

1. Filtering Data: The code filters out levels with an average score of zero to ensure only meaningful data is visualized.

2. Bar Chart Creation: A bar chart is generated to show the average score for each level. The x-axis is labeled with the actual level names.

3. Pie Chart Creation: A pie chart is created to display the distribution of players across score categories ('Low', 'Medium', 'High'), with a legend for clarity.

Bar chart:

<img src='image\q3_barchart.png'>

Pie chart:

<img src='image\q3_piechart.png'>

## Question 4

```python
python q4.py
```

Explanation of the Code:

1. Function Definition: A function HIGHEST_SCORE_LEVEL is defined to take a player_id as input.
Data Filtering: The function filters the DataFrame from q1 to retrieve records corresponding to the specified player_id.

2. Highest Score Calculation: If the player has records, it identifies the highest score and the corresponding level achieved.

3. Result Presentation: The result is presented as a DataFrame, showing the highest score and level, or an error message if the player is not found.

*Use player_id 104 as an example

Result:

<img src='image\q4.png'>