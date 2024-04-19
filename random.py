#Janiya Barrett
#4/18/24
#P5HW
#Math quiz - random number

#main menu
def main_menu(menu_list):
    print("Welcome to Math Quiz")
    print()
    print("MAIN MENU")
    print("--------------")
    print(f'1. Adding Random Numbers')
    print(f'2. Subtracting Random Numbers')
    print(f'3. Exit')
    choice = int(input("Please choose on of the menu options: "))
    while choice != 3:
        if choice == 1:
            return add_num
            print(add_num)
        if choice == 2:
            return subtract_num
            print(subtract_num)

            
    
    

    
'''  
# adding random numbers
def add_num(dictionary):
    import random
    num1 = random.randrange(1, 1000)
    num2 = random.randrange(1, 1000)
    print(num1)
    print(f'+{num2}')
    add_answer = num1 + num2
    
#subtracting random numbers
def subtract_num(dictionary):
    import random
    num3 = random.randrange(1, 1000)
    num4 = random.randrange(1, 1000)
    print(num3)
    print(f'-{num4}')
    subtract_answer = num3 - num4

    


def main():
    main()
'''
