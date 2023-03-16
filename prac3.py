
from collections import deque

def bfs_distance(graph, start, end):
    # initialize distances and parents to infinity and None
    distances = {v: float('inf') for v in graph}
    parents = {v: None for v in graph}

    # initialize distance from start vertex to itself to 0
    distances[start] = 0

    # use a deque to keep track of the nodes to visit
    queue = deque([start])

    while queue:
        node = queue.popleft()

        # iterate over the neighbors of the current node
        for neighbor, weight in graph[node]:
            # if we haven't visited the neighbor before
            if distances[neighbor] == float('inf'):
                # update its distance and parent
                distances[neighbor] = distances[node] + weight
                parents[neighbor] = node
                queue.append(neighbor)

    # backtrack from end node to start node to construct path
    path = []
    node = end
    while node is not None:
        path.append(node)
        node = parents[node]
    path.reverse()

    # return the distance and path
    return distances[end], path
    
# new delhi 0
# mumbai 1
# lucknow 2
# hyderabad 3
# kolkata 4
# benga 5
    
graph = {
    0: [(1, 5), (2, 2)],
    1: [(0, 5), (3, 2),(5,3)],
    2: [(0, 2), (3, 4), (4, 3)],
    3: [(2, 4), (1, 2),(4,3),(5,1)],
    4: [(5, 6),(2,3),(3,3)],
    5: [(1, 3),(4,6),(3,1)]
}

 # tracking distance between delhi(0) and bengaluru(5)   
distance, path = bfs_distance(graph, 0, 4)
print(distance)  
print(path)   # outputs teh path in form of indexes assigned to cities above  

