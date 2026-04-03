def wrdcnt():
    f=open("woff.txt","r")
    s=f.read()
    c=0
    a=s.split()
    for i in a:
        c+=1
    print(c)
wrdcnt()