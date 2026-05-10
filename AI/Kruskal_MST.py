# Kruskal's Minimum Spanning Tree Algorithm
#1. Sort all edges by weight
#2. Pick smallest edge
#3. If no cycle forms → include edg
#4. Repeat until V-1 edges selected
#Time--O(E log E)
#space-0(V+E)
#Rank means:

#Tree height/depth
class Graph:

    def __init__(self, vertices):

        self.V = vertices
        self.graph = []

    # Add edge
    def addEdge(self, u, v, w):

        self.graph.append([u, v, w])

    # Find parent
    def find(self, parent, i):

        if parent[i] == i:

            return i

        return self.find(parent, parent[i])

    # Union of sets
    def union(self, parent, rank, x, y):

        xroot = self.find(parent, x)
        yroot = self.find(parent, y)

        if rank[xroot] < rank[yroot]:

            parent[xroot] = yroot

        elif rank[xroot] > rank[yroot]:

            parent[yroot] = xroot

        else:

            parent[yroot] = xroot
            rank[xroot] += 1

    # Kruskal Algorithm
    def KruskalMST(self):

        result = []

        i = 0
        e = 0

        # Sort edges by weight
        self.graph = sorted(
            self.graph,
            key=lambda item: item[2]
        )

        parent = []
        rank = []

        # Create subsets
        for node in range(self.V):

            parent.append(node)
            rank.append(0)

        # MST contains V-1 edges
        while e < self.V - 1:

            u, v, w = self.graph[i]

            i += 1

            x = self.find(parent, u)
            y = self.find(parent, v)

            # Avoid cycle
            if x != y:

                e += 1

                result.append([u, v, w])

                self.union(parent, rank, x, y)

        # Print MST
        minimumCost = 0

        print("Edges in MST\n")

        for u, v, weight in result:

            minimumCost += weight

            print(u, "--", v, "==", weight)

        print("\nMinimum Spanning Tree Cost =", minimumCost)


# Driver Code
g = Graph(4)

g.addEdge(0, 1, 10)
g.addEdge(0, 2, 6)
g.addEdge(0, 3, 5)
g.addEdge(1, 3, 15)
g.addEdge(2, 3, 4)

# Function Call
g.KruskalMST()