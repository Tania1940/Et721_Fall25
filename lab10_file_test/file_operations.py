"""
Tania Akthar
Oct 15,2025
Lab 10, file operation test
"""

def write_file(filename, msg):
    with open(filename, "w") as file:
        file.write(msg)
 
def read_file(filename):
    with open(filename, "r") as file:
        file.readlines()

def append_file(filename):
    with open(filename, "a") as file:
        file.write("\nNew line added.")

# function from exercise lab 7 (yesterday)
"""
 create a function, named email_read(), that reads a txt file and returns the number of users that have @gmail, @yahoo, and @hotmail email address.
"""