num = int(input())

graph =[[] for i in range(num)]
for i in range(num):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)
    