a=int(input("Enter start of range="))
b=int(input("Enter end of range="))
c=0
for i in range (a,b+1):
    for j in range(2,i):
        if(i%j==0):
            c+=2
            break
        elif(i%j!=0):
            c=0
    if(i==1):
        continue
    if(c==0):
        print(i)
    elif(c>=1):
        continue