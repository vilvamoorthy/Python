user_input = input("Enter the phrase: ")
text = user_input.split()
a = "This is your Acronyms: "

for i in text:
    a += (i[0].upper())
print(a)

