"""
Tania Akthar
Sep 15, 2025
lab 5, functions
"""

"""
- pre-defined function: Python library
- user defined function: create by the programmer

what is function?
- block of code that begins with 'def' floows by the name of the function and parentheses()
- The body of the function is indented after the: 
- The body of the function only runs when the function is called.
- To call a funtion, we need to write the funtion's name and parentheses
"""
# import python file
from lab5_Akthar_function import *

# call function product()
print("\n----- Example 1: intro function -----")
n1 = 2
n2 = 5
p = product(n1, n2)
print(f"The product of {n1} and {n2} is {p}")
p = product()
print(f"The product is {p}")
p = product(5)
print(f"The product is {p}")

print("\n----- Example 2: function to calculate the hypotenuse -----")
s1 = 5
s2 = 3
hyp = hypotenuse(s1, s2)
print(f"The hypotenuse is {hyp:0.2f}")

print(
    "\n----- Example 3: function to check if the number is positive, negative, or zero. -----"
)
c = check_number(-3)
print(f"The number is {c}")
c = check_number(5)
print(f"The number is {c}")
c = check_number(0)
print(f"The number is {c}")

print("\n----- Example 4: function in a list -----")
grades = [50, 60, 85, 93, 72, 98]
avg = check_grades(grades)
print(f"Did i pass the class? {check_pass(avg)}")
grades = [50, 60, 30, 50]
print(f"Did i pass the class? {check_pass(check_grades(grades))}")
