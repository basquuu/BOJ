string = input()
count = 'abcdefghijklmnopqrstuvwxyz'
for i in count:
    if i in string:
        print(string.index(i), end=" ")
    else:
        print(-1, end=" ")