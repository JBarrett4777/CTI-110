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
overtime = (hours - 40)
reg_hours = (hours - overtime)
#finish this!!!!! (Probably finished it already!)
overtime_pay = (overtime * pay_rate)
reg_pay = (reg_hours * pay_rate)
gross_pay = (reg_pay + overtime_pay)
txt1 = "Hours Worked"
txt2 = "Pay Rate"
txt3 = "OverTime"
txt4 = "OverTime Pay"
txt5 = "RegHour Pay"
txt6 = "Gross Pay"

print("----------------------------------------")
print(f"Employee name: {name}")
print()

print(f'{txt1:<15}{txt2:<10}{txt3:<10}{txt4:<15}{txt5:<15}{txt6:<15}')
print("--------------------------------------------------------------------------------")
#FINISH OUTPUT!!!!
print(f'{hours:<15}{pay_rate:<10}')
