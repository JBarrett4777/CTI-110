#Janiya Barrett
#3/15/24
#P3HW1
#Fixing code

# This program takes a number grade , determines average and displays letter grade for average.

# Enter grades for six modules

mod_1 = float(input('Enter grade for Module 1: '))
mod_2 = float(input('Enter grade for Module 2: '))
mod_3 = float(input('Enter grade for Module 3: '))
mod_4 = float(input('Enter grade for Module 4: '))
mod_5 = float(input('Enter grade for Module 5: '))
mod_6 = float(input('Enter grade for Module 6: '))

# add grades entered to a list

grade_list = [mod_1, mod_2, mod_3, mod_4, mod_5, mod_6]
# TO DO: determine lowest, highest , sum and average for grades

list_min = min(grade_list)
list_max = max(grade_list)
list_sum = sum(grade_list)
list_length = len(grade_list)
list_avg = list_sum/list_length

# determine letter grade for average
print()
print("------------Results------------")
print(f"Lowest Grade: {list_min}")
print(f"Highest Grade: {list_max}")
print(f"Sum of Grades: {list_sum}")
print(f"Average: {list_avg:.2f}")
print("----------------------------------------")


if list_avg >= 90:
 print("Your grade is: A")

elif list_avg >= 80:
 print("Your grade is: B")

elif list_avg >= 70:
 print("Your grade is: C")

elif list_avg >= 60:
 print("Your grade is: D")

else:
 print("Your grade is :F")