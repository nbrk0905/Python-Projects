#Simple calculator project
def add(a,b):
    return a+b
def minus(a,b):
    return a-b
def mul(a,b):
    return a*b
def div(a,b):
    return a/b
option=True
while(option):
    a=float(input("Enter 1st number: "))
    b=float(input("Enter 2nd number: "))
    c=input("Enter the operation: ")
    if(c=="+"):
        print(f"{a} + {b} = {add(a,b)}")
    elif(c=="-"):
        print(f"{a} - {b} = {minus(a,b)}")
    elif(c=="*"):
        print(f"{a} x {b} = {mul(a,b)}")
    elif(c=="/"):
        if(b==0):
            print("Error!, Division by zero not possible")
        else:    
            print(f"{a}/{b} = {div(a,b)}")
    else:
        print("invalid operation")
    d=input("Want to continue,Type Y/N: ")
    if(d=="Y" or d=="y"):
        option==True
    else:
        option=False
print("End of program")        
