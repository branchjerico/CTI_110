# -*- coding: utf-8 -*-
"""P2HW2.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1z0AF8g2FDSqx9UTYr1Fqwa-IQsE4EmPY
"""

# Create an empty list to store grades
module_grades = []

# Prompt the user to enter grades for each module
module_grades.append(float(input("Enter grade for Module 1: ")))
module_grades.append(float(input("Enter grade for Module 2: ")))
module_grades.append(float(input("Enter grade for Module 3: ")))
module_grades.append(float(input("Enter grade for Module 4: ")))
module_grades.append(float(input("Enter grade for Module 5: ")))
module_grades.append(float(input("Enter grade for Module 6: ")))

# Calculate required values
lowest_grade = min(module_grades)
highest_grade = max(module_grades)
sum_of_grades = sum(module_grades)
average_grade = sum_of_grades / len(module_grades)

# Display the results in the required format

print("-"*9 + " Results " + "-"*9)

print(f"{'Lowest Grade:':<20} {lowest_grade}")
print(f"{'Highest Grade:':<20} {highest_grade}")
print(f"{'Sum of Grades:':<20} {sum_of_grades}")
print(f"{'Average Grade:':<20} {average_grade:.2f}")
print("-" * 30)