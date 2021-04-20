x = int(input("Enter the number: "))

if x > 1:
    # check for factors
    for i in range(2, x):
        if (x % i) == 0:
            print(x, " is not prime number")
            break
    else:
        print(x, " is prime number")
            
