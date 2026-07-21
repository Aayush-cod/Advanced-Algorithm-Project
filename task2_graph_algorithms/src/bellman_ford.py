from graph import Graph


def bellman_ford(graph: Graph, source, track_steps=False):
    distances = {node: float('inf') for node in graph.nodes()}
    predecessors = {node: None for node in graph.nodes()}
    distances[source] = 0

    all_edges = graph.edges()
    n = graph.num_nodes()
    steps = []

    for i in range(n - 1):
        updated = False
        for u, v, w in all_edges:
            if distances[u] != float('inf') and distances[u] + w < distances[v]:
                distances[v] = distances[u] + w
                predecessors[v] = u
                updated = True

        if track_steps:
            steps.append({"pass": i + 1, "distances": distances.copy()})

        if not updated:
            break

    has_negative_cycle = False
    for u, v, w in all_edges:
        if distances[u] != float('inf') and distances[u] + w < distances[v]:
            has_negative_cycle = True
            break

    if track_steps:
        return distances, predecessors, has_negative_cycle, steps
    return distances, predecessors, has_negative_cycle
