from collections import deque


def bfs(n, adj, start):
    ans=[]
    queue=deque()
    visited=[0]*n

    queue.append(start)
    visited[start]=1

    while len(queue)!=0:
        e=queue.popleft()
        ans.append(e)

        for neighbour in adj[e]:
            if visited[neighbour]==0:
                queue.append(neighbour)
                visited[neighbour]=1

    return ans

#recursive dfs--> in this  we first marks visited and then we will call the dfs for all the neighbours of the node
def dfs(node, result, visited, adj):
    visited[node]=1
    result.append(node)

    for neighbour in adj[node]:
        if visited[neighbour]==0:
            dfs(neighbour, result, visited, adj)
n=6
adj_list=[
   [1,2], #0
   [0,3,4],#1
   [0,5],#2
   [1],#3
   [1], #4
   [2]#5
]
visited=[0]*n
result=[]
print("bfs: "+ str(bfs(n,adj_list,0)))
dfs(0,result,visited,adj_list)
print("dfs: "+ str(result))