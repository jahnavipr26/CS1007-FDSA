class Graph:
    def __init__(self):
        self.adj_list = {}

    def add_edge(self, u, v):
        if u not in self.adj_list:
            self.adj_list[u] = []
        if v not in self.adj_list:
            self.adj_list[v] = []
        self.adj_list[u].append(v)
        self.adj_list[v].append(u)

    def dfs(self, start_vertex):
        visited = set()
        traversal_order = []

        def dfs_recursive(vertex):
            visited.add(vertex)
            traversal_order.append(vertex)
            for neighbor in self.adj_list.get(vertex, []):
                if neighbor not in visited:
                    dfs_recursive(neighbor)

        dfs_recursive(start_vertex)
        print("DFS Traversal Order:", traversal_order)


g = Graph()
g.add_edge(0, 1)
g.add_edge(0, 2)
g.add_edge(1, 3)
g.add_edge(2, 4)
g.add_edge(3, 5)

g.dfs(0)
