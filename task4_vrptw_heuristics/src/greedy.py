from vrptw import distance


def greedy_construction(instance):
    unvisited = list(instance.customers)
    routes = []
    for _ in range(instance.num_vehicles):
        if not unvisited:
            break
        route = []
        current_pos = instance.depot
        current_time = 0.0
        current_load = 0
        while True:
            best_customer = None
            best_dist = float('inf')
            for customer in unvisited:
                if current_load + customer.demand > instance.vehicle_capacity:
                    continue
                travel = distance(current_pos, customer)
                arrival = current_time + travel
                start_service = max(arrival, customer.ready_time)
                if start_service > customer.due_time:
                    continue
                if travel < best_dist:
                    best_dist = travel
                    best_customer = customer
            if best_customer is None:
                break
            route.append(best_customer)
            travel = distance(current_pos, best_customer)
            arrival = current_time + travel
            current_time = max(arrival, best_customer.ready_time) + best_customer.service_time
            current_load += best_customer.demand
            current_pos = best_customer
            unvisited.remove(best_customer)
        if route:
            routes.append(route)
    return routes, unvisited
