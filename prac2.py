# set the maximum capacities of the two jugs and the goal amount
jug1_max = 4
jug2_max = 3
goal = 2

# initialize the visited set to keep track of explored states, and the queue with the initial state
visited = set()
queue = [(0, 0, [])]

# use a while loop to explore states in the queue until the goal state is found or all states have been explored
while queue:
    # get the next state in the queue
    jug1, jug2, path = queue.pop(0)
    # if the state has already been visited, skip it
    if (jug1, jug2) in visited:
        continue
    # mark the state as visited
    visited.add((jug1, jug2))
    # if the state is the goal state, print the path and break out of the loop
    if jug1 == goal or jug2 == goal:
        print(path + [(jug1, jug2)])
        break
    # if the state is not the goal state, generate all possible next states
    # by considering all possible actions (filling a jug, emptying a jug, or pouring one jug into another)
    queue.append((jug1_max, jug2, path + [(jug1, jug2)]))
    queue.append((jug1, jug2_max, path + [(jug1, jug2)]))
    queue.append((0, jug2, path + [(jug1, jug2)]))
    queue.append((jug1, 0, path + [(jug1, jug2)]))
    pour_amt = min(jug1, jug2_max - jug2)
    queue.append((jug1 - pour_amt, jug2 + pour_amt, path + [(jug1, jug2)]))
    pour_amt = min(jug2, jug1_max - jug1)
    queue.append((jug1 + pour_amt, jug2 - pour_amt, path + [(jug1, jug2)]))
else:
    # if no solution is found, print a message saying so
    print("No solution found.")
