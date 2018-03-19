#-*-coding: utf-8-*-
graph = {}

N, M, V = map(int,raw_input().split(' '))

#generate dictionary
for i in range(N): graph[str(i+1)] = []
for i in range(M):
    d1, d2 = map(str,raw_input().split(' '))
    graph[d1].append(d2)
    graph[d2].append(d1)


def BFS(graph, root, N):
  visited = [] # 방문한 곳을 기록
  queue = [root] # 큐에 시작점을 줄세움

  while queue: # queue 가 빌 때 까지 탐색을 계속
    vertex = queue.pop(0) # 큐의 맨 앞의 원소를 방문할 꼭짓점으로 설정

    if vertex not in visited: # 꼭짓점이 방문된 적이 없다면 방문 기록에 추가
      visited.append(vertex)
      if (len(visited) == N):
          return visited

      for node in graph[vertex]: # 꼭짓점에 연결된 노드들 중
        if node not in visited: # 방문 안 된 곳 만을
          queue.append(node) # 큐에 줄세움

  return visited

def DFS(graph, root, N):
    stack = []
    visited = []

    stack.extend(root)
    while(stack):
        outputFromStack = stack.pop()
        visited.extend(outputFromStack)
        if (len(visited) == N):
          return visited

        inputToStack = list(set(graph[outputFromStack]) - set(visited))
        inputToStack.sort()
        inputToStack = inputToStack[::-1]
        stack.extend(inputToStack)
    return visited


print ' '.join(DFS(graph, str(V), N))
print ' '.join(BFS(graph, str(V), N))
