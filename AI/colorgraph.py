# Graph Coloring Problem

# Adjacency Matrix
g = [
[0,1,1,0,1],
[1,0,1,1,0],
[1,1,0,1,1],
[0,1,1,0,1],
[1,0,1,1,0]
]

# Node names
node = "abcde"

# Dictionary for node index
t = {}

for i in range(len(g)):

    t[node[i]] = i

# Degree of nodes
degree = []

for i in range(len(g)):

    degree.append(sum(g[i]))

# Possible colors
colorDict = {}

for i in range(len(g)):

    colorDict[node[i]] = [
        "Blue",
        "Red",
        "Yellow"
    ]

# Sort nodes by degree
sortedNode = []

index = []

for i in range(len(degree)):

    max_ = -1

    for j in range(len(degree)):

        if j not in index:

            if degree[j] > max_:

                max_ = degree[j]

                idx = j

    index.append(idx)

    sortedNode.append(node[idx])

# Final Solution
theSolution = {}

# Coloring process
for i in sortedNode:

    setTheColor = colorDict[i]

    theSolution[i] = setTheColor[0]

    adj_node = g[t[i]]

    for j in range(len(adj_node)):

        if adj_node[j] == 1:

            if setTheColor[0] in colorDict[node[j]]:

                colorDict[node[j]].remove(setTheColor[0])

# Print solution
for t,w in sorted(theSolution.items()):

    print("Node",t,"=",w)