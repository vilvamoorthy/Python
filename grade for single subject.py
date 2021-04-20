# enter the Marks:
a = int(input("Enter the number: "))
if a >= 75:
    print("Distinction")
elif a <= 75 and a >= 60:
    print("First class")
elif a <= 60 and a >= 40:
    print("Second class")
else:
    print("Fail")
