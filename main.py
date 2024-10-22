def calculator():
    print("THE BEST Calculator")
    print("Operations:")
    print("1= Addition")
    print("2= Multplication")
    
    choice = input("choose operation (1/2): ")
    
    if choice not in ['1', '2']:
        print("Invalid choice")
        return

    num1 = float(input("enter the first number: "))
    num2 = float(input("enter the second number: "))

    if choice == '1':
        result = num1 + num2
        print(f" {num1} + {num2} = {result}")
    elif choice == '2':
        result = num1 * num2
        print(f" {num1} * {num2} = {result}")


