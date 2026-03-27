stop = 0
while stop == 0:
    menu = input("Choose what you what to do: 1. Addition, 2. Subtraction and 3. Stop")

    if menu == "3":
        break
    
    number1 = input("enter a number: ")
    number2 = input("enter another number: ")

    number1 = int(number1)
    number2 = int(number2)

    if menu == "1": 
        result = number1 + number2

    if menu == "2":
        result = number1 - number2
    

    print(f"your total number are {result}")

print("The calculator have been turned off. please restart the file to begin again.")
