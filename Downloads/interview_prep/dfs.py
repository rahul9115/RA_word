from collections import defaultdict

class Graph:
    def __init__(self):
        self.graph=defaultdict(list)
    def addEdge(self,u,v):
        self.graph[u].append(v)
    def DFS(self,visited,start):
        visited[start]=True
        print(start,end=" ")
        am=self.graph[start]
        print(am)
        for i in am:
            if visited[i]==False:
                self.DFS(visited,i)
if __name__=="__main__":
    g = Graph()
    g.addEdge(0, 1)
    g.addEdge(0, 2)
    g.addEdge(1, 2)
    g.addEdge(2, 0)
    g.addEdge(2, 3)
    g.addEdge(3, 3)
    
    print("Following is Depth First Traversal")
    visited=[False]*4
    g.DFS(visited,0)



    

