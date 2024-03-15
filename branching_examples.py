#Branching - if, elif, else

num = 5
'''
#if/else statement
if num > 5:
    print("Greater than 5")
else:
    print("Less than or equal to 5")

#If num IS NOT EQUAL TO 5
if num != 5:
    print(f"Num is NOT 5, it is {num}")
else:
    print("Num is 5")

#If num IS EQUAL TO 5
if num == 5:
    print("Num is 5")
    num +=1
    print(f"num is now {num}")
else:
    print(f"Num is NOT 5, it is {num}")


name = "Bob"
age = 50

if name == "Bob":
    print("Hi, Bob")
    if age > 35:
        print("Wow, you're a little old")
    else:
        print("You're a youngin")
else:
    print("You're not Bob!")
'''

#elif statement

grade = 85

if grade >= 90:
    print("A")

elif grade >= 80:
    print("B")

elif grade >= 70:
    print("C")

else: #if grade is 69 or lower
    print("Your grade is kinda low")



