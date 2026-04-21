#Simple calculator with the help of functions
def add():
    c=a+b
    print(c)
def sub():
    c=a-b
    print(c)
def mul():
    c=a*b
    print(c)
def mul():
    c=a*b
    print(c)
def div():
    c=a/b
    print(c)
a=int(input("Enter a number="))
b=int(input("Enter a number="))
ch=input("choose from (+,-,x,/) =")
if ch=="+":
    add()
elif ch=="-":
    sub()
elif ch=="*":
    mul()
elif ch=="/":
    div()