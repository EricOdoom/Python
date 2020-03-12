def dfs(graph, start):
    stack = [start]
    visited = set()
    while stack:
        vertex = stack.pop()
        if vertex not in visited:
            visited.add(vertex)
            stack.extend(graph[vertex]-visited)
    return visited

def dfs_recursive(graph, start, visited=None):
    if visited is None:
        visited = set()
    visited.add(start)
    for next in graph[start] - visited:
        dfs_paths(graph, next, visited)
    return visited

def dfs_paths(graph, start, end):
    stack = [(start, [start])]
    all_paths = []
    while stack:
        (vertex, path) = stack.pop()
        for next in graph[vertex] - set(path):
            if next == end:
                all_paths.append(path + [next])
            else:
                stack.append((next, path+[next]))
    shortest_path = min(all_paths)
    return all_paths, shortest_path




graph = {'A' : set(['B', 'C']),
         'B': set(['D']),
          'C': set(['E']),
           'D': set('F'),
           'E':set(['G']),
           'G':set(['H', 'F']),
            'F': set(),
            'H':set()}

print(dfs_paths(graph, 'A', 'F'))
