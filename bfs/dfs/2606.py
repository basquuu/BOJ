import sys
input = sys.stdin.readline

num = int(input()) #컴퓨터 개수
connect = int(input()) #연결선 개수 

tmp =[[0] * (num+1) for i in range(num+1)] #그래프 초기화 
visited = [0 for i in range(num+1)] #방문한 컴퓨터 표시
count = 0

for i in range(connect):
    x, y = map(int,input().split())
    tmp[x][y] =1 #인접 행렬 방식
    tmp[y][x] =1

def dfs(i):
    visited[i] = 1
    global count 
    for a in range(num):
        if not visited[a] and tmp[i][a] ==1:
            dfs(a)
            count +=1
    return count

dfs(1)
print(count)