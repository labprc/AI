import heapq   # used for min heap (priority queue)

#u=current node, v=neighbor, w=weight of edge u-v


# Prim's Algorithm Function
def prim(n, graph):

    # Track visited nodes
    visited = [False] * n

    # Min heap stores (weight, node)
    # Start from node 0 with weight 0
    min_heap = [(0, 0)]

    # Total MST cost
    total = 0

    # Store MST edges
    mst = []

    # Run until heap becomes empty
    while min_heap:

        # Get minimum weight edge
        #It pop smallest edges of current node and add to the heap, so we get the smallest edge in the heap
        weight, u = heapq.heappop(min_heap)

        # If node already visited, skip
        # (avoids cycle)
        if visited[u]:
            continue

        # Mark node as visited
        visited[u] = True

        # Add edge weight to total MST cost
        total += weight

        # Check all neighbors of current node
        for v, w in graph[u]:

            # If neighbor not visited
            if not visited[v]:

                # Add edge into heap
                #in heap we store (weight, node) to prioritize by weight
                heapq.heappush(min_heap, (w, v))# it means current node u is connected to neighbor v with weight w, so we add (w, v) to the heap

                # Store MST edge
                mst.append((u, v, w))

    # Return MST edges and total cost
    return mst, total


# Graph using adjacency list
# Format:
# node : (neighbor, weight)

graph = {
    0: [(1, 4), (2, 3)],
    1: [(0, 4), (2, 1), (3, 2)],
    2: [(0, 3), (1, 1), (3, 4)],
    3: [(1, 2), (2, 4)]
}

# Number of vertices
n = 4

# Call Prim's Algorithm
mst, total = prim(n, graph)# it means we call the prim function with number of vertices and the graph, and it returns the edges in the MST and the total weight of the MST

# Print MST edges
print("MST Edges:")
for u, v, w in mst:
    print(u, "-", v, "=", w)

# Print total minimum cost
print("Total Weight =", total)