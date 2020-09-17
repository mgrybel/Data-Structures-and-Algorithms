import math
from queue import PriorityQueue


def shortest_path(graph, start, goal):
    path = PriorityQueue()
    path.put(start, 0)
    cost = {start: 0}
    came_from = {start: None}

    while not path.empty():
        current_path = path.get()
        if current_path == goal:
            calculate_route(came_from, start, goal)

        for node in graph.roads[current_path]:
            update_cost = cost[current_path] + distance(
                graph.intersections[current_path],
                graph.intersections[node]
            )

            if node not in cost or update_cost < cost[node]:
                cost[node] = update_cost
                total_cost = update_cost + distance(
                    graph.intersections[current_path], graph.intersections[node])
                path.put(node, total_cost)
                came_from[node] = current_path

    return calculate_route(came_from, start, goal)


def calculate_route(came_from, start, goal):
    current_path = goal
    path = [current_path]
    while current_path != start:
        current_path = came_from[current_path]
        path.append(current_path)
    path.reverse()
    return path


def distance(start, goal):
    return math.sqrt(((start[0] - goal[0]) ** 2) + ((start[1] - goal[1]) ** 2))
