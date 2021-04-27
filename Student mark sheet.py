class student:
    def __init__(self, pRoll_no, pname, pm1, pm2, pm3, pm4, pm5):
        self.Roll_no = pRoll_no
        self.name = pname
        self.m1 = pm1
        self.m2 = pm2
        self.m3 = pm3
        self.m4 = pm4
        self.m5 = pm5

    def marks(self):
        print("Roll number of the student: ", self.Roll_no)
        print("Name of the student: ", self.name)
        print("Tamil mark: ", self.m1)
        print("english mark: ", self.m2)
        print("maths mark: ", self.m3)
        print("science mark: ", self.m4)
        print("social mark: ", self.m5)

    def total(self):
        x = (m1 + m2 + m3 + m4 + m5)
        y = (m1 + m2 + m3 + m4 + m5)/5
        print("The total marks of ", self.name, "is ", x)
        print("The Average of ", self.name, "is ", y,"%")
        if m1 >= 35 and m2 >= 35 and m3 >= 35 and m4 >= 35 and m5 >= 35:
            print(self.name, " is pass")
        else:
            print(self.name, " is fail")

# Initially Roll_no is None:
Roll_no = None
# Using while loop for iteration:
while Roll_no != 0:
    print("Please enter 1 upto 20")
    Roll_no = int(input("Enter the Roll_no: "))
    Roll_no += 1
    # Using if condition for 10 student:
    if Roll_no >= 22 or Roll_no <= 1:
        print("------------End of the Mark sheet----------------")
        break
    name = input("Enter the name of the student: ")
    m1 = int(input("Enter the tamil mark: "))
    m2 = int(input("Enter the english mark: "))
    m3 = int(input("Enter the maths mark: "))
    m4 = int(input("Enter the science mark: "))
    m5 = int(input("Enter the social mark: "))

    Stu_obj = student(Roll_no, name, m1, m2, m3, m4, m5)
    Stu_obj.marks()
    Stu_obj.total()

    print()
