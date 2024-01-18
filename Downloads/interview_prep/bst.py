
    
class Node:
    def __init__(self,data):
        self.data=data
        self.right=None
        self.left=None
    
def addNode(root,d):
    print(d)
    if root==None:
        root=Node(d)
        return root
    elif root.data>d:
        root.left=addNode(root.left,d)
    else:
        root.right=addNode(root.right,d)
    return root

    

def display(queue,root):
    # if (root!=None):
    #     display(queue,root.left)
    #     print(root.data,"\n")
    #     display(queue,root.right)
    if root.left!=None:
        queue.append(root.left)
    if root.right!=None:
        queue.append(root.right)
    print(root.data,"\n")
    if len(queue)==0:
        return
    else:
        display(queue,queue.pop(0))

def printBoundary(root):
    if root==None:
        return
    if root.left==None and root.right==None:
        print(root.data)
        return 
    else:
        printBoundary(root.left)
        printBoundary(root.right)
        
def printBoundaryleft(root):
    if root==None:
        return
    if root.left!=None:
        print(root.data)
        printBoundaryleft(root.left)
    elif root.right!=None:
        print(root.data)
        printBoundaryleft(root.right)

    
def printBoundaryright(root):
    if root==None:
        return
    if root.right!=None:
        printBoundaryright(root.right)
        print(root.data)
    elif root.left!=None:
        printBoundaryright(root.left)
        print(root.data)
   
    
def boundary_traversal(root):
    print(root.data,end=" ")
    printBoundaryleft(root.left)
    printBoundary(root.left)
    printBoundary(root.right)
    printBoundaryright(root.right)


def diagonal_traversal(root,d,diagonal):
    
    if root==None:
        return
    
    if diagonal.get(d)!=None:
        diagonal[d].append(root)
    else:
        diagonal[d]=[root]

    diagonal_traversal(root.left,d+1,diagonal)
    diagonal_traversal(root.right,d,diagonal)
    


    


if __name__=="__main__":
    
    root=None
    queue=[]
    root=addNode(root,50)
    root=addNode(root,30)
    root=addNode(root,20)
    root=addNode(root,40)
    root=addNode(root,70)
    root=addNode(root,60)
    root=addNode(root,80)
    display(queue,root)
    print("Boundary Traversal")
    boundary_traversal(root)
    diagonal={}
    # diagonal_traversal(root,0,diagonal)
    # print("Diagonal Elements are")
    # for i,j in diagonal.items():
    #     print(f"Diagonal {i}")
    #     for k in j:
    #         print(k.data)


