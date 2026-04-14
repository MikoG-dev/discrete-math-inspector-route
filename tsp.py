import itertools

class Node:
    def __init__(self, node_id):
        self.id = node_id
        self.connections = {} 

    def add_connection(self, target_id, distance):
        self.connections[target_id] = distance

def solve_tsp_full():
    node_ids = ['A', 'B', 'C', 'D', 'E', 'F', 'G']
    nodes = {nid: Node(nid) for nid in node_ids}

    edges = [
        ('A', 'B', 21), ('A', 'C', 15), ('A', 'D', 27),
        ('B', 'C', 18), ('B', 'E', 14),
        ('C', 'D', 11), ('C', 'E', 20), ('C', 'F', 16),
        ('D', 'F', 28), ('D', 'G', 31),
        ('E', 'F', 19), ('E', 'G', 28),
        ('F', 'G', 22)
    ]

    for u, v, dist in edges:
        nodes[u].add_connection(v, dist)
        nodes[v].add_connection(u, dist)

    stations_to_visit = ['B', 'C', 'D', 'E', 'F', 'G']
    all_perms = list(itertools.permutations(stations_to_visit))

    min_distance = float('inf')
    optimal_routes = []
    
    print(f"{'Attempt':<10} | {'Route Map':<40} | {'Status/Distance'}")
    print("-" * 75)

    for i, perm in enumerate(all_perms, 1):
        route_list = ['A'] + list(perm) + ['A']
        route_str = " -> ".join(route_list)
        
        current_distance = 0
        is_valid = True

        for j in range(len(route_list) - 1):
            u, v = route_list[j], route_list[j+1]
            if v in nodes[u].connections:
                current_distance += nodes[u].connections[v]
            else:
                is_valid = False
                break 

        # Display Logic
        if is_valid:
            status = f"{current_distance} km"
            if current_distance < min_distance:
                min_distance = current_distance
                optimal_routes = [route_str]
            elif current_distance == min_distance:
                optimal_routes.append(route_str)
        else:
            status = "INVALID"

        if i % 10 == 0 or is_valid: 
            print(f"{i:<10} | {route_str:<40} | {status}")

    print("\n" + "="*40)
    print("FINAL OPTIMAL RESULTS")
    print(f"Minimum Distance: {min_distance} km")
    print("Optimal Routes Found:")
    for r in optimal_routes:
        print(f" >> {r}")

if __name__ == "__main__":
    solve_tsp_full()