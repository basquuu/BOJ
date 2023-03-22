import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

def dfs(x):
    visit[x] = 1
    for i in graph[x]:
        if not visit[i]:
            dfs(i)
     # 재귀 함수 제한 시간 풀기
n, m = map(int, input().split())
graph = [[] for i in range (n+1)] #nxn 빈 행렬 만들기
visit = [0] * (n+1)
for _ in range(m):
    a, b = map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)
    
link = 0 #연결 요소의 개수
for i in range(1,n+1):
    if not visit[i]:
        link += 1
        dfs(i)
print(link)
