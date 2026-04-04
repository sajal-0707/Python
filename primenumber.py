num=int(input("Enter a number to check if it's prime or composite="))
count=0
for i in range(2,num):
    if(num%i==0):
        count+=1
    elif(num%i!=0):
        continue
if(count==0):
    print("prime")
elif(count>=1):
    print("composite")