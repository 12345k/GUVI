import itertools
n,k = map(int, input().split())
l=len(str(n))-k
list_arr=[]
for subset in itertools.combinations(str(n), l):
    a=''.join(map(str,subset))
    list_arr.append(int(a))
print(min(list_arr))