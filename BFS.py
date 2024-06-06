from queue import Queue

def bfs(graph, start):
    visited = {node: False for node in graph}
    Q = Queue()
    Q.put(start)
    visited[start] = True

    while not Q.empty():
        n = Q.get()
        print(n, end=" ")

        for u in graph[n]:
            if not visited[u]:
                Q.put(u)
                visited[u] = True

graph = {
    'V0': ['V1', 'V2'],
    'V1': ['V0', 'V2', 'V3'],
    'V2': ['V0', 'V1','V3','V4'],
    'V3': ['V1','V2','V4','V5'],
    'V4': ['V2', 'V3','V4'],
    'V5': ['V3', 'V4']
}

start = 'V0'

bfs(graph, start)
    