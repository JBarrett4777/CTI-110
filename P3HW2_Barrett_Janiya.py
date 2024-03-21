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
#Variables
name = input("Enter employee's name: ")
hours = float(input("Enter number of hours worked: "))
pay_rate = float(input("Enter employee's pay rate: "))
overtime_rate = (pay_rate * 1.5)

if hours > 40:
    overtime = (hours - 40)
    reg_hours = (hours - overtime)
else:
    overtime = 0
    reg_hours = (hours - overtime)

overtime_pay = (overtime * overtime_rate)
reg_pay = (reg_hours * pay_rate)
gross_pay = (reg_pay + overtime_pay)

print("----------------------------------------")
print(f"Employee name: {name}")
print()
print(f"{'Hours Worked':<15}{'Pay Rate':<10}{'OverTime':<10}{'OverTime Pay':<15}{'RegHour Pay':<15}{'Gross Pay':<15}")
print("--------------------------------------------------------------------------------")
print(f'{hours:<15}${pay_rate:<10}{overtime:<10}${overtime_pay:<15.2f}${reg_pay:<15.2f}${gross_pay:<10.2f}')