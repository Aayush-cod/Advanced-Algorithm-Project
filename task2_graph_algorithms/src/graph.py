class Graph:
    def __init__(self):
        self.adj = {}

    def add_node(self, node):
        if node not in self.adj:
            self.adj[node] = []

    def add_edge(self, u, v, weight):
        self.add_node(u)
        self.add_node(v)
        self.adj[u].append((v, weight))

    def nodes(self):
        return list(self.adj.keys())

    def edges(self):
        result = []
        for u in self.adj:
            for v, w in self.adj[u]:
                result.append((u, v, w))
        return result

    def neighbors(self, u):
        return self.adj.get(u, [])

    def num_nodes(self):
        return len(self.adj)

    def num_edges(self):
        return sum(len(v) for v in self.adj.values())

    def __repr__(self):
        lines = []
        for u in self.adj:
            for v, w in self.adj[u]:
                lines.append(f"  {u} -> {v}  (weight={w})")
        return f"Graph({self.num_nodes()} nodes, {self.num_edges()} edges)\n" + "\n".join(lines)
