n = int(input())
array = []
for i in range(n):
    a,b = map(int,input().split())
    array.append([b,a])
array.sort()
for i in range(n):
    print(array[i][1],array[i][0])
    