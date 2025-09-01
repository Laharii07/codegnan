#importing all modules

import addition
import subtraction
import multipication
import division
import modulodivision

operations = ('1.Addition\n',
              '2.Subtraction\n',
              '3.Multiplication\n',
              '4.Division\n',
              '5.Modulodivision\n'
            )

# main function

if __name__ == '__main__':
    print("Welcome to basic calculator, it will perform  basic calculations between 2 numbers only")
    print(*operations)
    while True:
        choice = int(input("select your operation from 1-5:"))
        if choice ==1:
            x = int(input("Enter the first number: "))
            y = int(input("Enter the second number: "))
            print(addition.add(a =x, b = y))
        elif choice ==2:
            x = int(input("Enter the first number"))
            y = int(input("Enter the second number"))
            print(subtraction.sub(a =x, b = y))
        elif choice == 3:
            x = int(input("Enter the first number"))
            y = int(input("Enter the second number"))
            print(multipication.mult(a =x, b = y))
        elif choice == 4:
            x = int(input("Enter the first number"))
            y = int(input("Enter the second number"))
            print(division.div(a =x, b = y))
        elif choice == 5:
            x = int(input("Enter the first number"))
            y = int(input("Enter the second number"))
            print(modulodivision.mod_div(a =x, b = y))
        elif choice == 6:
            print("Exiting form calculator")
            exit()
        else:
            print("Please enter the number between 1 to 5")
        

