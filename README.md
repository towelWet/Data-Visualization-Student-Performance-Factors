# Student Performance Factors Visualization

## Overview

This project visualizes student performance data sourced from the [Student Performance Factors dataset on Kaggle](https://www.kaggle.com/datasets/lainguyn123/student-performance-factors/discussion?sort=hotness). The dataset contains various factors that could influence student exam scores, such as study time, attendance, parental involvement, and access to resources.

The purpose of this project is to analyze and visualize the relationships between these factors and student performance, making it easier to gain insights into what affects students' exam scores.

## Dataset

The dataset contains the following columns:

- **Hours_Studied**: The number of hours a student spends studying per week.
- **Attendance**: The percentage of classes attended.
- **Parental_Involvement**: The level of involvement of parents (Low, Medium, High).
- **Access_to_Resources**: Whether the student has access to learning resources.
- **Extracurricular_Activities**: Participation in extracurricular activities (Yes/No).
- **Sleep_Hours**: The number of hours the student sleeps per night.
- **Previous_Scores**: The student's score in previous exams.
- **Motivation_Level**: The student's level of motivation (Low, Medium, High).
- **Internet_Access**: Whether the student has internet access (Yes/No).
- **Tutoring_Sessions**: The number of tutoring sessions attended by the student.
- **Family_Income**: The family's income level (Low, Medium, High).
- **Teacher_Quality**: The perceived quality of teaching (Poor, Average, Good).
- **School_Type**: Type of school (Public/Private).
- **Peer_Influence**: The level of influence peers have on the student (Low, Medium, High).
- **Physical_Activity**: The number of hours the student engages in physical activity per week.
- **Learning_Disabilities**: Whether the student has learning disabilities (Yes/No).
- **Parental_Education_Level**: The education level of the parents (Low, Medium, High).
- **Distance_from_Home**: The distance from the student's home to school (Near, Moderate, Far).
- **Gender**: The gender of the student (Male/Female).
- **Exam_Score**: The student's exam score.

## Project Structure

- **students.py**: The main Python script that loads the dataset, generates various visualizations, and saves them as images.
- **StudentPerformanceFactors.csv**: The dataset file containing student performance data.
- **README.md**: This file.

## How to Get Started

### Prerequisites

- Python 3.7+
- Required Python libraries:
  - pandas
  - matplotlib
  - seaborn

You can install the required libraries using the following command:
```bash
pip install pandas matplotlib seaborn
```

### Running the Code

1. Download this repository and make sure both `students.py` and `StudentPerformanceFactors.csv` are in the same folder.
2. Navigate to the folder in your terminal:
   ```bash
   cd path/to/your/folder
   ```
3. Run the Python script:
   ```bash
   python students.py
   ```

The script will generate multiple visualizations based on the data and save them as `.png` files in the same directory.

## What the Code Does

The code generates the following visualizations:

1. **Exam Scores Distribution**: A histogram showing the distribution of student exam scores.
2. **Study Time vs Exam Score**: A scatter plot that visualizes the relationship between the number of hours spent studying and the exam score.
3. **Correlation Heatmap**: A heatmap showing the correlations between various numerical factors (e.g., study hours, attendance, previous scores, etc.) and their relationship with the exam score.
4. **Attendance vs Average Exam Score**: A bar chart displaying the average exam score based on different attendance percentages.
5. **Exam Scores by Gender**: A box plot comparing exam scores across genders.
6. **Pair Plot**: A pair plot showing relationships between key performance-related variables, such as exam score, previous scores, and study time.

These visualizations help understand how different factors impact student performance, allowing for deeper analysis of what drives better exam scores.

## Insights

By running this project, you'll get the following insights:
- How attendance affects student performance.
- Whether study time is correlated with higher exam scores.
- How factors like parental involvement, motivation level, and access to resources might play a role in performance.
- Whether there are differences in performance based on gender.

For more information and discussion on the dataset, visit the [Kaggle Discussion](https://www.kaggle.com/datasets/lainguyn123/student-performance-factors/discussion?sort=hotness).

---
