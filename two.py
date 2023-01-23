f=open('f2.txt')
f2=open('f2b.txt','w')
p=0
for i in f:
    if(p%2==0):
        f2.write(str(i))
    p=p+1
f.close()
f2.close()
f2=open('f2b.txt','r')
for i in f2:
    print(i)