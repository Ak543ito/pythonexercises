user_input_number = int(input("Please enter any number."))

mod = user_input_number % 2

multi_four = user_input_number % 4

if mod > 0:
    print("You picked an odd number!")
else:
    print("You picked an even number!")

if multi_four == 0:
    print("Your number is a multiple of 4")
else:
    print("")

num = int(input("Pls enter a number you want to check!"))
check = int(input("Enter the number u want to check with"))

checking = num % check

if checking == 0:
    print("The number is even!")
else:
    print("The number is odd!")








