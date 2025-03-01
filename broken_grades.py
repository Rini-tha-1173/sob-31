# Calculating Grades (ok, let me think about this one)

# Write a program that will average 3 numeric exam grades, return an average test score, a corresponding letter grade, and a message stating whether the student is passing.

# Average	Grade
# 90+	A
# 80-89	B
# 70-79	C
# 60-69	D
# 0-59	F

# Exams: 89, 90, 90
# Average: 90
# Grade: A
# Student is passing.

# Exams: 50, 51, 0
# Average: 33
# Grade: F
# Student iis failing.

exam_one = int(input("Input exam grade one: "))

exam_two = int(input("Input exam grade two: ")) # RR: adding the int data type

exam_three= int(input("Input exam grade three: ")) # RR: changing the name from exam_3 to exam_three
                                                # and str to int

grades = [exam_one, exam_two, exam_three] # RR: adding the ',' between each values
sum = 0
for grade in grades: # RR: changing grade to grades
  sum = sum + grade

avg = sum / len(grdes)

if avg >= 90:
    letter_grade = "A"
elif avg >= 80 and avg < 90: # RR: adding the ':'
    letter_grade = "B"
elif avg > 69 and avg < 80:
    letter_grade = "C" # RR: changing the quotes from ' to "
elif avg <= 69 and avg >= 60: # RR: changing the value from 65 to 60
    letter_grade = "D"
else: # RR: changing elif to else
    letter_grade = "F"

print("Exam: " + (grades)) # RR: change grade to grades

print("Average: " + str(avg))

print("Grade: " + letter_grade)
# RR: removed the indentation for the print statements
if letter_grade== "F": # RR: changing letter-grade to letter_grade and changing is to '=='
    print("Student is failing.") # RR: adding the parenthesis
else:
    print("Student is passing.") #RR: adding the parenthesis
