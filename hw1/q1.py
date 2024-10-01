import pandas as pd
import os

# Load the uploaded CSV file to check its contents
file_path = 'w02_data_to_st.csv'
data = pd.read_csv(file_path)

# Show the first few rows of the data
data.head()


#Question 1

import matplotlib.pyplot as plt

# Calculate the overall and location-based average scores
overall_avg = round(data['Score'].mean(), 2)
location_avg = data.groupby('Location')['Score'].mean().round(2)

# Visualize the results
plt.figure(figsize=(8, 5))

# Plot overall average
plt.axhline(y=overall_avg, color='r', linestyle='--', label=f'Overall Avg: {overall_avg}')

# Plot location-based averages
location_avg.plot(kind='bar', color='skyblue')

# Add labels and title
plt.title('Average Chinese Score by Location')
plt.xlabel('Location')
plt.ylabel('Average Score')
plt.legend()

# Show the plot
plt.tight_layout()
plt.show()


#Question 2

def convert_to_grade(score):
    if score >= 80:
        return 'A'
    elif score >= 60:
        return 'B'
    elif score >= 40:
        return 'C'
    elif score >= 20:
        return 'D'
    else:
        return 'E'

# Apply the function to the data
data['Grade'] = data['Score'].apply(convert_to_grade)

# Count the distribution of grades
grade_distribution = data['Grade'].value_counts().sort_index()

# Plot the grade distribution
plt.figure(figsize=(8, 5))
grade_distribution.plot(kind='bar', color='lightcoral')

# Add labels and title
plt.title('Distribution of Grades (A-E)')
plt.xlabel('Grade')
plt.ylabel('Number of Students')

# Show the plot
plt.tight_layout()
plt.show()

# Calculate grade distribution by location
location_grade_distribution = data.groupby('Location')['Grade'].value_counts().unstack().fillna(0)

# Plot the location-based grade distribution
location_grade_distribution.plot(kind='bar', stacked=True, figsize=(8, 5), colormap='Set3')

# Add labels and title
plt.title('Grade Distribution by Location')
plt.xlabel('Location')
plt.ylabel('Number of Students')

# Show the plot
plt.tight_layout()
plt.show()

# Average grade level (based on a simplified numeric equivalent for each grade)
grade_numeric = {'A': 5, 'B': 4, 'C': 3, 'D': 2, 'E': 1}
data['Grade Numeric'] = data['Grade'].map(grade_numeric)

# Calculate the overall average grade and the equivalent letter grade
overall_grade_avg_numeric = data['Grade Numeric'].mean()
overall_grade_avg = round(overall_grade_avg_numeric, 2)

# Determine which letter grade range the average falls into
for grade, value in grade_numeric.items():
    if overall_grade_avg >= value:
        avg_grade_range = grade
        break

overall_grade_avg, avg_grade_range


#Question 3
# Step 3: Convert scores to grades based on the mean score X as the new baseline

# Define the mean score X
X = overall_avg

# New grade boundaries based on X
def convert_to_dynamic_grade(score, X):
    if score >= X + 26:
        return 'A'
    elif score >= X + 6:
        return 'B'
    elif X - 5 <= score <= X + 5:
        return 'C'
    elif score >= X - 23:
        return 'D'
    else:
        return 'E'

# Apply the dynamic grading function
data['Dynamic_Grade_1'] = data['Score'].apply(lambda s: convert_to_dynamic_grade(s, X))

# Count the dynamic grade distribution
dynamic_grade_distribution_1 = data['Dynamic_Grade_1'].value_counts().sort_index()

# Plot the dynamic grade distribution (method 1)
plt.figure(figsize=(8, 5))
dynamic_grade_distribution_1.plot(kind='bar', color='lightgreen')

# Add labels and title
plt.title('Dynamic Grade Distribution (Method 1)')
plt.xlabel('Grade')
plt.ylabel('Number of Students')

# Show the plot
plt.tight_layout()
plt.show()

# Dynamic grade distribution by location
location_dynamic_grade_distribution_1 = data.groupby('Location')['Dynamic_Grade_1'].value_counts().unstack().fillna(0)

# Plot the location-based dynamic grade distribution (method 1)
location_dynamic_grade_distribution_1.plot(kind='bar', stacked=True, figsize=(8, 5), colormap='Set2')

# Add labels and title
plt.title('Dynamic Grade Distribution by Location (Method 1)')
plt.xlabel('Location')
plt.ylabel('Number of Students')

# Show the plot
plt.tight_layout()
plt.show()

# Calculate the average dynamic grade level (method 1)
data['Dynamic_Grade_1 Numeric'] = data['Dynamic_Grade_1'].map(grade_numeric)

# Calculate the overall average dynamic grade
overall_dynamic_grade_avg_numeric_1 = data['Dynamic_Grade_1 Numeric'].mean()
overall_dynamic_grade_avg_1 = round(overall_dynamic_grade_avg_numeric_1, 2)

# Determine the average grade range (method 1)
for grade, value in grade_numeric.items():
    if overall_dynamic_grade_avg_1 >= value:
        avg_dynamic_grade_range_1 = grade
        break

overall_dynamic_grade_avg_1, avg_dynamic_grade_range_1


#Question 4
# Step 4: Convert scores to grades based on a new X+16, X+6... scheme

# New dynamic grade boundaries (method 2) based on X
def convert_to_dynamic_grade_2(score, X):
    if score >= X + 16:
        return 'A'
    elif score >= X + 6:
        return 'B'
    elif X - 5 <= score <= X + 5:
        return 'C'
    elif score >= X - 13:
        return 'D'
    else:
        return 'E'

# Apply the dynamic grading function (method 2)
data['Dynamic_Grade_2'] = data['Score'].apply(lambda s: convert_to_dynamic_grade_2(s, X))

# Count the dynamic grade distribution (method 2)
dynamic_grade_distribution_2 = data['Dynamic_Grade_2'].value_counts().sort_index()

# Plot the dynamic grade distribution (method 2)
plt.figure(figsize=(8, 5))
dynamic_grade_distribution_2.plot(kind='bar', color='lightblue')

# Add labels and title
plt.title('Dynamic Grade Distribution (Method 2)')
plt.xlabel('Grade')
plt.ylabel('Number of Students')

# Show the plot
plt.tight_layout()
plt.show()

# Dynamic grade distribution by location (method 2)
location_dynamic_grade_distribution_2 = data.groupby('Location')['Dynamic_Grade_2'].value_counts().unstack().fillna(0)

# Plot the location-based dynamic grade distribution (method 2)
location_dynamic_grade_distribution_2.plot(kind='bar', stacked=True, figsize=(8, 5), colormap='Set1')

# Add labels and title
plt.title('Dynamic Grade Distribution by Location (Method 2)')
plt.xlabel('Location')
plt.ylabel('Number of Students')

# Show the plot
plt.tight_layout()
plt.show()

# Calculate the average dynamic grade level (method 2)
data['Dynamic_Grade_2 Numeric'] = data['Dynamic_Grade_2'].map(grade_numeric)

# Calculate the overall average dynamic grade (method 2)
overall_dynamic_grade_avg_numeric_2 = data['Dynamic_Grade_2 Numeric'].mean()
overall_dynamic_grade_avg_2 = round(overall_dynamic_grade_avg_numeric_2, 2)

# Determine the average grade range (method 2)
for grade, value in grade_numeric.items():
    if overall_dynamic_grade_avg_2 >= value:
        avg_dynamic_grade_range_2 = grade
        break

overall_dynamic_grade_avg_2, avg_dynamic_grade_range_2

