import sys
input = sys.stdin.readline
n = int(input())
array = [0] * 10001
for i in range(n):
    num = int(input())
    array[num] += 1
for i in range(10001):
    if array[i] != 0:
        for j in range(array[i]):
            print(i)
