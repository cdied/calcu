#calcu app with 2 input and 4 function
#addition
def addition(x, y):
    return x + y
#subtract
def subtract(x , y):
    return x - y
#multiplcation
def multipn(x, y):
    return x * y
#divition
def divition(x, y):
    return x / y
###
##choise that can be made
#print("1. Addition")
#print("2. Subtract")
#print("3. multipon")
#print("4. division")
##choice input
#choice = input("> ")
##num1, num2 input
#num1 = int(input("Enter 1st number: "))
#num2 = int(input("Enter 2nd number: "))
##if statsmentfor choses
#if choice == "1":
#    print(num1,"+",num2,"=",addition(num1,num2))
#elif choice == "2":
#    print(num1,"-",num2,"=",subtract(num1,num2))
#elif choice == "3":
#    print(num1,"*",num2,"=",multipn(num1,num2))
#elif choice == "4":
#    print(num1,"/",num2,"=",divition(num1,num2))
#else:
#    print("Invailed Syntex") #will exectue once.#
###


running = True

while running:
    print("""
    1. addition
    2. subtaction
    3. multiplcation
    4. divition
    5 QUIT
    """)
    choice_1 = input("> ")
    num_1 = float(input("Enter Your 1st Number: "))
    num_2 = float(input("Enter your 2nd Number: "))
    if choice_1 == "1":
        print(num_1, "+", num_2, "=", addition(num_1, num_2))
    elif choice_1 == "2":
        print(num_1,"-",num_2,"=",subtract(num_1,num_2))
    elif choice_1 == "3":
        print(num_1,"*",num_2,"=",multipn(num_1,num_2))
    elif choice_1 == "4":
        print(num_1,"/",num_2,"=",divition(num_1,num_2))
    elif choice_1 == "5":
        break
    else:
        print("Invailed Syntex")

