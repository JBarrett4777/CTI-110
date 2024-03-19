#Janiya Barrett
# 3/19/24
# P3HW2
# Branching
'''
Asks the user to enter name of employee
Ask user to enter number of hours the employee worked this week
Ask user to enter employee's pay rate
Evaluate if employee has worked overtime (more than 40 hours).
If yes, calculate the amount owed to employee for overtime hours
Calculate amount employee should be paid for regular hours worked.
Display gross pay 
'''

name = input("Enter employee's name: ")
hours = float(input("Enter number of hours worked: "))
pay_rate = float(input("Enter employee's pay rate: "))
overtime = (hours - 40)

print("----------------------------------------")
print(f"Employee name: {name}")
print()
print(f'Hours Worked {hours: <15}')
if hours > 40:
    print(f"OverTime {overtime}")
else:
    print("None")

#figure out the formatting
print("Hours Worked    Overtime Pay")
print(f'{hours:<15}{overtime}')
