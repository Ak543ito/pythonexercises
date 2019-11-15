print("Hello!")
user_number = int(input("Pls enter a number to divide with: "))

listRange = list(range(1,user_number+1))

divisorList = []

for number in listRange:
    if user_number % number == 0:
        divisorList.append(number)

print(divisorList)
