import math
import random


class Customer:
    def __init__(self, id, x, y, demand, ready_time, due_time, service_time=0):
        self.id = id
        self.x = x
        self.y = y
        self.demand = demand
        self.ready_time = ready_time
        self.due_time = due_time
        self.service_time = service_time

    def __repr__(self):
        return f"Customer({self.id}, demand={self.demand}, window=[{self.ready_time},{self.due_time}])"


def distance(c1, c2):
    return math.hypot(c1.x - c2.x, c1.y - c2.y)


class VRPTWInstance:
    def __init__(self, depot, customers, vehicle_capacity, num_vehicles):
        self.depot = depot
        self.customers = customers
        self.vehicle_capacity = vehicle_capacity
        self.num_vehicles = num_vehicles

    def all_nodes(self):
        return [self.depot] + self.customers


def generate_vrptw_instance(n_customers, vehicle_capacity=100, num_vehicles=5, seed=42):
    rng = random.Random(seed)
    depot = Customer("Depot", 50, 50, 0, 0, 1000, 0)
    customers = []
    for i in range(n_customers):
        x, y = rng.randint(0, 100), rng.randint(0, 100)
        demand = rng.randint(5, 30)
        ready = rng.randint(0, 400)
        due = ready + rng.randint(50, 200)
        service = rng.randint(5, 15)
        customers.append(Customer(f"C{i}", x, y, demand, ready, due, service))
    return VRPTWInstance(depot, customers, vehicle_capacity, num_vehicles)


def route_feasible(route, instance):
    total_demand = sum(c.demand for c in route)
    if total_demand > instance.vehicle_capacity:
        return False, None, None
    current_time = 0.0
    current_pos = instance.depot
    total_dist = 0.0
    arrival_times = []
    for customer in route:
        travel = distance(current_pos, customer)
        arrival = current_time + travel
        start_service = max(arrival, customer.ready_time)
        if start_service > customer.due_time:
            return False, None, None
        arrival_times.append(start_service)
        current_time = start_service + customer.service_time
        total_dist += travel
        current_pos = customer
    total_dist += distance(current_pos, instance.depot)
    return True, total_dist, arrival_times


def solution_total_distance(routes, instance):
    total = 0.0
    for route in routes:
        feasible, dist, _ = route_feasible(route, instance)
        if not feasible:
            return None
        total += dist
    return total
