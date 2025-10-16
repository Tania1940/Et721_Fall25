"""
Tania Akthar
Oct 8, 2025
Lab 9, test input and output data
"""
# function to collect students' grade and returns the average of the grades
def main():
    # collect the amount students
    while True:
        try:
            num_students = int(input("Enter number of students: "))
            if num_students <=0:
                print("Number of stuents must be greater than 0. Please try again")
            else:
                break
        except ValueError:
            print("Invalid input. Plase enter a positive number")

    # collect the grades for each student
    total_sum_grades = 0
    for i in range(num_students):
        while True:
            try:
                grade = float(input(f"Enter grade for student {i+1}: "))
                if 0<=grade<=100:
                    total_sum_grades += grade
                    break
                else:
                    print("s ")
            except ValueError:
                print("Invalid input! Enter a numerical value")
    # calculate for the average grade
    average = total_sum_grades / num_students
    # print reasult
    print(f"The class average is {average:.2f}")

#EXERCISE
def exercise_invalid_inputs():
    try:
        # invalid student number input
        num_students = int("Peter")
    except ValueError:
        print("Error: please enter a number for students.")

    try:
        # invalid grade input
        grade = float("Peter")
    except ValueError:
        print("Error: please enter a valid number grade.")