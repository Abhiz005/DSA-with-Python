def dfs(graph, start):
    visited = {node: False for node in graph}
    stack = [start]
    visited[start] = True

    while stack:
        node = stack[-1]
        stack.pop()
        print(node, end=" ")

        for neighbor in graph[node]:
            if not visited[neighbor]:
                stack.append(neighbor)
                visited[neighbor] = True

graph = {
    'V0': ['V1', 'V2'],
    'V1': ['V0', 'V2', 'V3'],
    'V2': ['V0', 'V1','V3','V4'],
    'V3': ['V1','V2','V4','V5'],
    'V4': ['V2', 'V3','V4'],
    'V5': ['V3', 'V4']
}

start = 'V0'

dfs(graph, start)

    