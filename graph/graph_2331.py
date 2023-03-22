n, m = map(int,input().split())
current = n
nums = [current]

while True:
    temp = str(current)
    num = 0
    for i in temp:
        num += int(i) ** m
        
    if num in nums:
        nums = nums[:nums.index(num)] #아니 천잰가 
        break
    else:
        nums.append(num)
        current = num
print(len(nums))

#큐 활용해서 문제 풀면 훨씬빠를듯 