from math import comb
n = int(input())

d = [0] * 1001
d[1] = 10
for i in range(2,n+1):
    d[i] = comb(10+i-1,i)
print(d[n]%10007)