T = int(input())
m , n, k = map(int, input().split())
graph = [[] for i in range(k+1)]
visited = []
for i in range(k):
    x , y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)
    
def dfs(i):
    visited [i] = 1
    for a in graph[i]:
        if not visited[a] and graph[i][a]:
            dfs(a)