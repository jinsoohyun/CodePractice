#-*-coding: utf-8-*-
#graph = {}

'''
N, M, V = raw_input().split(' ')
for
'''

graph = {'1': set(['2', '3', '4']),
         '2': set(['1', '4']),
         '3': set(['1', '4']),
         '4': set(['1', '3', '2'])
         }
'''
def dfs(graph, root):
  visited = [] # 각 꼭짓점(vertex)이 방문되었는지 기록
  stack = [root, ]
 
  while stack: # stack 이 비게 되면 탐색 끝
    vertex = stack.pop() # 방문되어지고 있는 꼭짓점
    if vertex not in visited: #
      visited.append(vertex)
      stack.extend(graph[vertex] - visited)
 
  return visited


'''

def dfs_recursive(graph, root, visited=None):
  if visited is None:
    visited = set()

  visited.add(root)

  # 주어진 root 과 연결되어 있는 다른 node 들에 대해 방문하지 않은 것들만 재귀 호출합니다.
  for node in graph[root] - visited:
      dfs_recursive(graph, node, visited)

  return visited



print (dfs_recursive(graph, '1'))
