#Janiya Barrett
#3/15/24
#P3HW1
#Fixing code

# This program takes a number grade , determines average and displays letter grade for average.

# Enter grades for six modules

mod_1 = input('Enter grade for Module 1: ')
mod_2 = input('Enter grade for Module 2: ')
mod_3 = input('Enter grade for Module 3: ')
mod_4 = input('Enter grade for Module 4: ')
mod_5 = input('Enter grade for Module 5: ')
mod_6 = input('Enter grade for Module 6: ')

# add grades entered to a list

grade_list = [mod_1, mod_2, mod_3, mod_4, mod_5, mod_6]
# TO DO: determine lowest, highest , sum and average for grades

list_min = min(grade_list)
list_max = max(grade_list)
list_sum = sum(grade_list)
list_length = len(grade_list)
list_avg = list_sum/list_length

# determine letter grade for average


if list_avg >= 90:
 print('Your grade is: A')
else:
 print()
if list_avg > 80:
 print('Your grade is: B')
else:
 print('')
if
print

else:
 print('Your grade is: F') #TO DO: Finish this