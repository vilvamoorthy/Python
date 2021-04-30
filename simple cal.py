print("simple pythone calculator")
a=int(input("enter your first value:"))
b=int(input("enter your second value:"))
print(" 1=+",'\n',"2=-",'\n',"3=*",'\n',"4=/",'\n',"5=%",'\n',"6=power")
c=int(input("mode of claculation:"))
def add_ab():
    print("result:",a+b)
def sub_ab():
    print("result:",a-b)
def mul_ab():    
    print("result:",a*b)
def div_ab():    
    print("result:",a/b)
def mod_ab():
    print("result:",a%b)
def pwo_ab():
    print("result:",a**b)        
if c==1:
    add_ab()
elif c==2:
    sub_ab()
if c==3:
    mul_ab()
elif c==4:
    div_ab()
if c==5:
    mod_ab()
elif c==6:
    pwo_ab()    