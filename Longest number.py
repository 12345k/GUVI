import itertools
n=int(input())
l=str(input())
l=l.replace(" ","")
list_arr=[]

for subset in itertools.permutations(str(l), len(l)):
    a=''.join(map(str,subset))
    list_arr.append(int(a))
print(max(list_arr))