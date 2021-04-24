import math
n=int(input())
p=0
q=0
if n%2==0:
    p=6**(n-1)
    q=6**n
else:
    p=6**(n-1)
    q=6**(n)
# print(p,q)
print(math.ceil((p/q) * 1000000007 ))