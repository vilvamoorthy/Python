# program for fibonacci sequence:

nterm = int(input("Enter number of terms: "))

# first two terms:

n1, n2 = 0, 1
count = 0

# check if the number of term is valid:

if nterm <= 0:
    print("Please enter the positive number: ")
elif nterm == 1:
    print("Fibonacci seqence upto ", nterm,": ")
    print(n1)
else:
    print("Fibonacci sequence upto: ", nterm)
    while count < nterm:
        print(n1)
        nth = n1 + n2
        #update values:
        n1 = n2
        n2 = nth
        count += 1
        
        
