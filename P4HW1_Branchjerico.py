# Jerico Branch
# 3/25/2025
# P4HW1
# Use nested loops to get valid grades from user


'''Pseudocode

Create variable num_scores (int) -> user input number of scores
Create an empty list -> scores_list
for each in range(num_scores)
    score = int(input(f"Enter score # {each+1}"))
    while score is invalid - less than 0 or score greater than 100
        output to user score is invalid
        output to user score must be 0-100
        score = int(input(f"Enter score # {each+1} again"))
    scores_list.append(score)
print scores_list to ensure correctness

Get the lowest score in list -> assign it to a variable
Remove the lowest score from the list

Get average of list after removing lowest score
Use average to determine letter grade
'''

# Get number of scores with validation
while True:
    try:
        num_scores = int(input("Enter the number of scores you would like to enter: "))
        if num_scores > 0:
            break
        print("Please enter a positive number.")
    except ValueError:
        print("Invalid input. Please enter a whole number.")

# Collect all scores with validation
scores_list = []
for i in range(num_scores):
    while True:
        try:
            # The variable 'i' is already defined in the for loop. We will use that instead of 'each'
            score = int(input(f"Enter score #{i+1}: "))  
            if 0 <= score <= 100:
                scores_list.append(score)
                break
            print("Invalid score. Score must be between 0 and 100.")
        except ValueError:
            print("Invalid input. Please enter an integer value.")

print("Scores Entered:", scores_list)


print("-" * 9 + "Results" + "-" *9)

# Find and remove lowest score
if scores_list:
    lowest_score = min(scores_list)
    print("Lowest score entered:", lowest_score)

    # Create new list without lowest score
    modified_scores = []
    lowest_removed = False
    for score in scores_list:
        if not lowest_removed and score == lowest_score:
            lowest_removed = True
            continue
        modified_scores.append(score)

    print("Score List after dropping lowest score:", modified_scores)

    # Calculate average and grade if scores remain
    if modified_scores:
        avg_score = sum(modified_scores) / len(modified_scores)
        print("Average of scores in modified list:", round(avg_score, 2))

        # Determine letter grade
        if avg_score >= 90:
            grade = 'A'
        elif avg_score >= 80:
            grade = 'B'
        elif avg_score >= 70:
            grade = 'C'
        elif avg_score >= 60:
            grade = 'D'
        else:
            grade = 'F'


        print("Letter Grade:", grade)
    else:
        print("No scores left after dropping the lowest score.")
else:
    print("No scores were entered.")
print("--" * 12)