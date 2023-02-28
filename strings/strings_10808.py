string = input()
count = [0] * 26
for i in string:
    count[ord(i)-97] +=1
print(*count)