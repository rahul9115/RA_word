from collections import deque, defaultdict

class Graph:
    def __init__(self):
        self.graph=defaultdict(list)
        self.queue=deque()
        self.visited=set()
    
    def addEdge(self,u,v):
        self.graph[u].append(v)
    
    def bfs(self,start):
        self.queue.append(start)
        self.visited.add(start)
        print(start)
        while self.queue:
            nodes=self.graph[self.queue.popleft()]
            for node in nodes:
                if node not in self.visited:
                    print(node)
                    self.queue.append(node)
                    self.visited.add(node)

if __name__=="__main__":
    g = Graph()
    g.addEdge(0, 1)
    g.addEdge(0, 2)
    g.addEdge(1, 2)
    g.addEdge(2, 0)
    g.addEdge(2, 3)
    g.addEdge(3, 3)
    
    print("Following is Breadth First Traversal")
    g.bfs(0)      


                


