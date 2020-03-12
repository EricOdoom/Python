def bfs(graph, start):
    queue = [start]
    visited = set()
    while queue:
        vertex = queue.pop(0)
        if vertex not in visited:
            visited.add(vertex)
            queue.extend(graph[vertex] - visited)
    return visited

def bfs_paths(graph, start, end):
    queue = [(start, [start])]
    all_paths = []
    while queue:
        (vertex, path) = queue.pop(0)
        for next in graph[vertex] - set(path):
            if next == end:
                all_paths.append(path + [next])
            else:
                queue.append((next, path+[next] ))
    return all_paths


def shortest(graph, start, end):
    paths = bfs_paths(graph, start, end)
    if paths:
        return paths[0]

graph = {'A' : set(['B', 'C']),
         'B': set(['D']),
          'C': set(['E']),
           'D': set('F'),
           'E':set(['G']),
           'G':set(['H', 'F']),
            'F': set(),
            'H':set()}

print(bfs(graph, 'A'))
print(bfs_paths(graph ,'A', 'F'))
print(shortest(graph, 'A', 'G'))
