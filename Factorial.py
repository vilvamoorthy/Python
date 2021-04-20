# max number for factorial
num = int(input("Enter the number: "))

# factorial start with:
factorial = 1

if num < 0:
    print("Plz enter the positive number: ")
elif num == 0:
    print("Factorial is 0 and 1")
else:
    for i in range(1 , num + 1):
        factorial = factorial*i
    print("The factorial of ",num, "is ", factorial)
