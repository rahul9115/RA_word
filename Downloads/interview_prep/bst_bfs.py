class Node:
    def __init__(self,d):
        self.left=None
        self.right=None
        self.data=d

def addNode(root,d):
    if not root:
        return Node(d)
    elif d<root.data:
        root.left=addNode(root.left,d)
    else:
        root.right=addNode(root.right,d)
    return root

def bfs_traversal(root,queue):
    print(root.data)
    if root.left!=None:
        queue.append(root.left)
    if root.right!=None:
        queue.append(root.right)
    if len(queue)!=0:
        bfs_traversal(queue.pop(0),queue)

root=addNode(None,8)
root=addNode(root,3)
root=addNode(root,10)
root=addNode(root,1)
root=addNode(root,6)
root=addNode(root,14)
root=addNode(root,13)

bfs_traversal(root,[])

    




