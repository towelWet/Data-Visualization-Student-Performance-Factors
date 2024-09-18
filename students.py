# students.py

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

# Get the current directory where the script is located
current_dir = os.path.dirname(os.path.abspath(__file__))

# Load the dataset
file_path = os.path.join(current_dir, 'StudentPerformanceFactors.csv')
data = pd.read_csv(file_path)

# Display basic information about the dataset
print("Dataset Info:")
print(data.info())
print("\nFirst 5 rows:")
print(data.head())

# 1. Visualize the distribution of exam scores
plt.figure(figsize=(8, 6))
data['Exam_Score'].hist(bins=20, color='skyblue', edgecolor='black')
plt.title('Exam Scores Distribution')
plt.xlabel('Exam Score')
plt.ylabel('Frequency')
plt.grid(False)
output_path = os.path.join(current_dir, 'exam_scores_distribution.png')
plt.savefig(output_path)
plt.show()

# 2. Scatter plot: Study time vs Exam score
plt.figure(figsize=(8, 6))
plt.scatter(data['Hours_Studied'], data['Exam_Score'], color='purple')
plt.title('Study Time vs Exam Score')
plt.xlabel('Hours Studied')
plt.ylabel('Exam Score')
plt.grid(True)
output_path = os.path.join(current_dir, 'study_time_vs_exam_score.png')
plt.savefig(output_path)
plt.show()

# 3. Correlation heatmap
plt.figure(figsize=(10, 8))
correlation_matrix = data.corr()
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', linewidths=0.5)
plt.title('Correlation Heatmap')
output_path = os.path.join(current_dir, 'correlation_heatmap.png')
plt.savefig(output_path)
plt.show()

# 4. Absences vs Exam score (Bar Plot)
plt.figure(figsize=(8, 6))
data.groupby('Attendance')['Exam_Score'].mean().plot(kind='bar', color='orange')
plt.title('Attendance vs Average Exam Score')
plt.xlabel('Attendance')
plt.ylabel('Average Exam Score')
plt.xticks(rotation=0)
output_path = os.path.join(current_dir, 'attendance_vs_exam_score.png')
plt.savefig(output_path)
plt.show()

# 5. Box plot: Exam scores by gender
plt.figure(figsize=(8, 6))
sns.boxplot(x='Gender', y='Exam_Score', data=data, palette='Set2')
plt.title('Exam Scores by Gender')
plt.xlabel('Gender')
plt.ylabel('Exam Score')
output_path = os.path.join(current_dir, 'exam_scores_by_gender.png')
plt.savefig(output_path)
plt.show()

# 6. Pair plot for performance scores and study time
sns.pairplot(data[['Exam_Score', 'Previous_Scores', 'Hours_Studied']])
output_path = os.path.join(current_dir, 'pair_plot.png')
plt.savefig(output_path)
plt.show()
