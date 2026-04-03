def ltecnt():
    a=input("Enter a letter to find it's number of occurrence in this file:")
    f=open("woff.txt","r")
    s=f.read()
    c=0
    for i in s:
        if i==a:
            c+=1
        else:
            continue
    print(a,"has occured",c,"times")
ltecnt()