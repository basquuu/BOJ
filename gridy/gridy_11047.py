n, k = map(int,input().split())
list = [int(input()) for _ in range(n)]
answer = 0
list.sort(reverse=True)
for money in list:
    answer += k//money #역순으로 나열했을 때의 몫
    k = k % money #나머지 업데이트
    if k == 0:
        break
print(answer)