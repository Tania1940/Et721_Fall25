"""
Tania Akthar
lab 7, accessing data in a file
Oct 14, 2025
"""
from lab7_function import *


print("\n ----- example 1: reading file -----")
read_data("phrases.txt")

print("\n ----- example 2: reading specific portion of a file -----")
read_up("phrases.txt")

print("\n ----- example 3: reading specific portion using readline -----")
read_readline("phrases.txt")

print("\n ----- example 4: reading specific portion using readlines -----")
read_all("phrases.txt")

print("\n ----- example 5: loop through each line -----")
read_each("phrases.txt")

print("\n ----- example 6: creating new file -----")
new_file("Akthar.txt")

print("\n ----- example 7: append data into an existing file -----")
stamp_date("Akthar.txt")

print("\n ----- EXERCISE -----")

count_yahoo = email_read("user_email.txt", "@yahoo")
print("yahoo =", count_yahoo)

count_gmail = email_read("user_email.txt", "@gmail")
print("gmail =", count_gmail)

count_hotmail = email_read("user_email.txt", "@hotmail")
print("hotmail =", count_hotmail)

write_report(count_gmail, count_yahoo, count_hotmail)



