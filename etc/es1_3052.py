list = []
for i in range(10):
    n = int(input())
    list.append(n%42)
list = set(list)
print(len(list))
#set함수는 중복 제거해준대