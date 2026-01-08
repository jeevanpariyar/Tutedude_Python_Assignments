#1. Grade Checker
#Take a score as input and print the grade based on the following:
'''
️Grade Checker Program
🔹 Problem Statement

Take a student’s score as input and print the grade based on conditions.

#🔹 Explanation

The program takes numeric input using input()

Uses if-elif-else conditions to check score ranges

Prints the corresponding grade
'''

print("Enter the score:")
score = int(input())
if score >= 90:
    print("Grade: A")
elif score >= 80:
    print("Grade: B")
elif score >= 70:
    print("Grade: C")
elif score >= 60:
    print("Grade: D")
else:
    print("Grade: F")
