import heapq
from graph import Graph


def to_undirected_adjacency(graph: Graph):
    undirected = {node: {} for node in graph.nodes()}
    for u, v, w in graph.edges():
        if v not in undirected[u] or w < undirected[u][v]:
            undirected[u][v] = w
        if u not in undirected[v] or w < undirected[v][u]:
            undirected[v][u] = w
    return undirected


def prim(graph: Graph, start=None, track_steps=False):
    undirected = to_undirected_adjacency(graph)
    nodes = graph.nodes()
    if not nodes:
        return ([], 0) if not track_steps else ([], 0, [])

    start = start or nodes[0]
    visited = {start}
    mst_edges = []
    total_weight = 0
    steps = []

    pq = []
    for v, w in undirected[start].items():
        heapq.heappush(pq, (w, start, v))

    while pq and len(visited) < len(nodes):
        w, u, v = heapq.heappop(pq)
        if v in visited:
            continue

        visited.add(v)
        mst_edges.append((u, v, w))
        total_weight += w

        if track_steps:
            steps.append({
                "edge_added": (u, v, w),
                "visited": visited.copy(),
                "mst_edges_so_far": mst_edges.copy()
            })

        for nxt, weight in undirected[v].items():
            if nxt not in visited:
                heapq.heappush(pq, (weight, v, nxt))

    return (mst_edges, total_weight) if not track_steps else (mst_edges, total_weight, steps)
