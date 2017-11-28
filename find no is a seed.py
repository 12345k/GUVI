n = int(input())
l = list(str(n))
ans =1
for i in l:
    ans = ans*int(i)
print(n," is a seed of ",n*ans)