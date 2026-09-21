from collections import *

def bfs(graph, index):
    visited = set()
    queue = deque([index])
    visited.add(index)
    while queue:
        pop = queue.popleft()
        print(pop)
        for i in graph[pop]:
            if i not in visited:
                queue.append(i)
                visited.add(i)
graph = {'a': ['b'], 'b': ['c'], 'c' : ['a']}
bfs(graph, 'a')
