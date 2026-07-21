import heapq
from graph import Graph


def dijkstra(graph: Graph, source, track_steps=False):
    distances = {node: float('inf') for node in graph.nodes()}
    predecessors = {node: None for node in graph.nodes()}
    distances[source] = 0

    visited = set()
    pq = [(0, source)]
    steps = []

    while pq:
        dist_u, u = heapq.heappop(pq)

        if u in visited:
            continue
        visited.add(u)

        if track_steps:
            steps.append({
                "finalized_node": u,
                "distances": distances.copy(),
                "visited": visited.copy()
            })

        for v, weight in graph.neighbors(u):
            if weight < 0:
                raise ValueError(f"Dijkstra's algorithm cannot handle negative edge weight: {u}->{v} = {weight}")
            new_dist = dist_u + weight
            if new_dist < distances[v]:
                distances[v] = new_dist
                predecessors[v] = u
                heapq.heappush(pq, (new_dist, v))

    if track_steps:
        return distances, predecessors, steps
    return distances, predecessors


def reconstruct_path(predecessors, source, target):
    if predecessors.get(target) is None and target != source:
        return None
    path = []
    node = target
    while node is not None:
        path.append(node)
        node = predecessors[node]
    path.reverse()
    return path if path[0] == source else None
