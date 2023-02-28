from collections import deque

def bfs(graph, node, visited):
    queue = deque([node]) #큐 구현 
    visited[node] = True
    
    #큐가 완전히 빌 때까지 반복
    while queue:
        v = queue.popleft()
        # 탐색 순서 출력
        print(v,end=' ')
        # 현재 처리 중인 노드에서 방문하지 않은 인접 노드 모두 큐에 삽입
        for i in graph([v]):
            if not (visited([i])):
                queue.append(i)
                visited[i] = True
# 노드별로 방문 정보를 리스트로 표현 
visited = [False] * 9