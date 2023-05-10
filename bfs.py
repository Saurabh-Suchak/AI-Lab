# from collections import deque

# def bfs_distance(graph, start, end):
#     # initialize distances and parents to infinity and None
#     distances = {v: float('inf') for v in graph}
#     parents = {v: None for v in graph}

#     # initialize distance from start vertex to itself to 0
#     distances[start] = 0

#     # use a deque to keep track of the nodes to visit
#     queue = deque([start])

#     while queue:
#         node = queue.popleft()

#         # iterate over the neighbors of the current node
#         for neighbor, weight in graph[node]:
#             # if we haven't visited the neighbor before
#             if distances[neighbor] == float('inf'):
#                 # update its distance and parent
#                 distances[neighbor] = distances[node] + weight
#                 parents[neighbor] = node
#                 queue.append(neighbor)

#     # backtrack from end node to start node to construct path
#     path = []
#     node = end
#     while node is not None:
#         path.append(node)
#         node = parents[node]
#     path.reverse()

#     # return the distance and path
#     return distances[end], path
    
# # new delhi 0
# # mumbai 1
# # lucknow 2
# # hyderabad 3
# # kolkata 4
# # benga 5
    
# graph = {
#     0: [(1, 5), (2, 2)],
#     1: [(0, 5), (3, 2),(5,3)],
#     2: [(0, 2), (3, 4), (4, 3)],
#     3: [(2, 4), (1, 2),(4,3),(5,1)],
#     4: [(5, 6),(2,3),(3,3)],
#     5: [(1, 3),(4,6),(3,1)]
# }

#  # tracking distance between delhi(0) and bengaluru(5)   
# distance, path = bfs_distance(graph, 0, 4)
# print(distance)  
# print(path)   # outputs teh path in form of indexes assigned to cities above  


# approach 2

from array import *
cost=[[0,3,2,-99,-99,5],
       [3,0,1,6,-99,-99],
       [2,1,0,3,4,-99],
       [-99,6,3,0,3,-99],
       [-99,-99,4,3,0,2],
       [5,-99,-99,-99,2,0]]
graph={
    'A':['B','C','F'],
    'B':['A','C','D'],
    'C':['A','B','D','E'],
    'D':['B','C','E'],
    'E':['C','D','F'],
    'F':['A','F']
}

#maintaing index and corresponding city
city_index={
    'A' :0,
    'B':1,
    'C':2,
    'D':3,
    'E':4,
    'F':5
}
# mumbai A
# bengaluru B
# lucknow E
# hyderabad C
# kolkata D
# new delhi F

visited=[]
queue=[]
route_cost=0
path=[]
def bfs(visited,graph,source,target):
  visited.append(source)
  queue.append(source)
  
  while queue:
    m=queue.pop(0)
    path.append(m)
    if m==target:
      break
    for adj in graph[m]:
      if adj not in visited :
        visited.append(adj)
        queue.append(adj)
def calculate_cost(path,route_cost):
  length = len(path)
  for i in range(1,length):
    route_cost=route_cost+ cost[city_index[path[i-1]]][city_index[path[i]]]
  print('Cost of a path is : ',route_cost)


#finding a path from new delhi to bengaluru
bfs(visited,graph,'F','B')

print('From Bengaluru to New Delhi Path : ',path)

#calculate cost of a path
calculate_cost(path,route_cost)