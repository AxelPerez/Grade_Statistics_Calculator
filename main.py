'''The program asks the user for results from different students on the course. These include exam points and 
numbers of exercises completed. The program then prints out statistics based on the results.'''


''' This function as the user to input two numbers, exam points, and number of exercises completed. The output is 
a list of list containing the exam points and number of exercises completed for each student'''
def ask_user_for_input():

    new_results = []

    while True:

        results = input("Exam points and exercises completed: ")
        if results == "":
            break
        else:
            # Split the input into a list
            results = results.split()
            # Convert the strings to integers
            results = [int(result) for result in results]
            # Append the list to the results list
            new_results.append(results)
            
    return new_results

# This function calculates the grade of each student based on the exam points and number of exercises completed        
def calculate_grade_points(results: list):
    # Create a new list to store the grades
    grades_points = []

    # Iterate over the results
    for result in results:
        # Calculate the grade
        grade_points = result[0] + result[1] // 10
        # Append the grade to the grades list
        grades_points.append(grade_points)

    return grades_points

# This function converts the grade points to grades
def convert_grade_points_to_grades(grades_points: list):
    # Create a new list to store the grades
    grades = []

    # Iterate over the grades points
    for grade_point in grades_points:
        # Convert the grade points to grades
        if grade_point > 27:
            grade = 5
        elif grade_point >= 24 and grade_point <= 27:
            grade = 4
        elif grade_point >= 21 and grade_point <= 23:
            grade = 3
        elif grade_point >= 18 and grade_point <= 20:
            grade = 2
        elif grade_point >= 15 and grade_point <= 17:
            grade = 1
        else:
            grade = 0
        # Append the grade to the grades list
        grades.append(grade)

    return grades

# This function calculates the average of the grades points
def calculate_points_average(grades_points: list):
    # Calculate the average of the grades points
    grade_average = sum(grades_points) / len(grades_points)

    return grade_average

def calculate_pass_percentage(grades: list):
    # Calculate the pass percentage
    pass_percentage = grades.count(0) / len(grades) * 100
    pass_percentage = (pass_percentage - 100)* -1

    return pass_percentage

# This function prints out the grade distribution
def grade_distribution(grades: list):
    
    print("5: ", end="")
    if 5 in grades:
        print("*" * grades.count(5), end="")
    print("\n4: ", end="")
    if 4 in grades:
        print("*" * grades.count(4), end="")
    print("\n3: ", end="")
    if 3 in grades:
        print("*" * grades.count(3), end="")
    print("\n2: ", end="")
    if 2 in grades:
        print("*" * grades.count(2), end="")
    print("\n1: ", end="")
    if 1 in grades:
        print("*" * grades.count(1), end="")
    print("\n0: ", end="")
    if 0 in grades:
        print("*" * grades.count(0))
    
def main():
    results = ask_user_for_input()
    grades_points = calculate_grade_points(results)
    grades = convert_grade_points_to_grades(grades_points)
    grade_average = calculate_points_average(grades_points)
    pass_percentage = calculate_pass_percentage(grades)

    print("Statistics:")
    print(f"Point average: {grade_average:.1f}")
    print(f"Pass percentage: {pass_percentage:.1f}")
    print("Grade distribution:")
    grade_distribution(grades)

main()