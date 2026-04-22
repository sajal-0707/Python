a=int(input("Enter number of stairs= "))
for i in range (a,0,-1):
    for i in range (1,i+1):
        print("*",end="")
    print("\n")