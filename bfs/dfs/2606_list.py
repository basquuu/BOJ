num = int(input())
connect = int(input())

graph = [[] for i in range(num+1)]
visited = [0] * (num+1)

for i in range(connect):
    a, b = map(int,input().split())
    graph[a] += [b]
    graph[b] += [a]
    
def dfs(i):
    visited[i] = 1
    for a in graph[i]:
        if not visited[a]:
            dfs(a)
dfs(1)
print(sum(visited)-1)