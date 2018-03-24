import os
l=[]
n=int(input())
for i in range(n):
    s = str(input())
    l.append(s)
print(os.path.commonprefix(l))
