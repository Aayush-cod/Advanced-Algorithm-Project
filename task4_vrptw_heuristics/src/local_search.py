from vrptw import route_feasible, solution_total_distance


def two_opt_route(route, instance):
    improved = True
    best_route = route[:]
    _, best_dist, _ = route_feasible(best_route, instance)

    while improved:
        improved = False
        for i in range(len(best_route) - 1):
            for j in range(i + 1, len(best_route)):
                candidate = best_route[:i] + best_route[i:j+1][::-1] + best_route[j+1:]
                feasible, dist, _ = route_feasible(candidate, instance)
                if feasible and dist < best_dist:
                    best_route = candidate
                    best_dist = dist
                    improved = True

    return best_route, best_dist


def inter_route_swap(routes, instance):
    routes = [r[:] for r in routes]
    improved = True

    while improved:
        improved = False
        current_total = solution_total_distance(routes, instance)

        for i, route_i in enumerate(routes):
            for c_idx, customer in enumerate(route_i):
                for j, route_j in enumerate(routes):
                    if i == j:
                        continue
                    for insert_pos in range(len(route_j) + 1):
                        new_route_i = route_i[:c_idx] + route_i[c_idx+1:]
                        new_route_j = route_j[:insert_pos] + [customer] + route_j[insert_pos:]

                        feasible_i, dist_i, _ = route_feasible(new_route_i, instance) if new_route_i else (True, 0, [])
                        feasible_j, dist_j, _ = route_feasible(new_route_j, instance)

                        if feasible_i and feasible_j:
                            trial_routes = routes[:]
                            trial_routes[i] = new_route_i
                            trial_routes[j] = new_route_j
                            trial_routes = [r for r in trial_routes if r]
                            trial_total = solution_total_distance(trial_routes, instance)

                            if trial_total is not None and trial_total < current_total:
                                routes = trial_routes
                                improved = True
                                current_total = trial_total
                                break
                    if improved:
                        break
                if improved:
                    break
            if improved:
                break

    return routes


def local_search(routes, instance):
    routes = [r[:] for r in routes]
    prev_total = solution_total_distance(routes, instance)
    while True:
        new_routes = []
        for route in routes:
            improved_route, _ = two_opt_route(route, instance)
            new_routes.append(improved_route)
        routes = new_routes

        routes = inter_route_swap(routes, instance)

        new_total = solution_total_distance(routes, instance)
        if new_total >= prev_total - 1e-9:
            break
        prev_total = new_total

    return routes
