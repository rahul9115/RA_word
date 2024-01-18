from collections import defaultdict
class Graph:
    def __init__(self):
        self.graph=defaultdict(list)
        self.queue=[]
    def addEdge(self,u,v):
        self.graph[u].append(v)
    def BFS(self,visited,start):
        self.queue.append(start)
        visited[start]=True
        while len(self.queue)!=0:
            val=self.queue.pop(0)
            print(val,end=" ")
            al=self.graph[val]
            for i in al:
                if visited[i]!=True:
                    visited[i]=True
                    self.queue.append(i)
if __name__=="__main__":
    g = Graph()
    g.addEdge(0, 1)
    g.addEdge(0, 2)
    g.addEdge(1, 2)
    g.addEdge(2, 0)
    g.addEdge(2, 3)
    g.addEdge(3, 3)
    
    print("Following is Breadth First Traversal")
    visited=[False]*4
    g.BFS(visited,0)



