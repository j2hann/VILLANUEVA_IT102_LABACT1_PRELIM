from calculator_module import *

try:
    print("Please select an operation. \n1 = Addition \n2 = Subtraction \n3 = Multiplication \n4 = Division \n5 = Exit")
    choice = int(input("Enter your choice: "))

    if choice == 5:
        print("Goodbye!")
        exit()
    elif choice < 1 or choice > 5:
        print("Invalid input. Must choose between 1-5.")
        exit()
    else:
        try:
            num1 = float(input("Enter your first number: "))
            num2 = float(input("Enter your second number: "))
        
            if choice == 4 and num2 == 0:
                print("Invalid input. Value must not be 0.")
                exit()
        except ValueError:
            print("Invalid input. Must be a numeric value.")
            exit()
    
    if choice == 1:
        result = add(num1, num2)
        print(f"The sum of {num1} and {num2} is {result}.")
    elif choice == 2:
        result = sub(num1, num2)
        print(f"The difference of {num1} and {num2} is {result}.")   
    elif choice == 3:
        result = mul(num1, num2)
        print(f"The product of {num1} and {num2} is {result}.")
    elif choice == 4:
        result = div(num1, num2)
        result = round(result, 2)
        print(f"The quotient of {num1} and {num2} is {result}.")

except ValueError:
    print("Invalid input. Must be a numeric value.")
    
