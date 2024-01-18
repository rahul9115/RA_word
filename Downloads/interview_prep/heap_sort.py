from copy import deepcopy
class Heap:
    def __init__(self,n):
        self.heap=[]
        self.heap_size=0
        self.capacity=n
    
    def parent(self,key):
        return int((key-1)/2)

    def left(self,key):
        return int(2*key+1)
    
    def right(self,key):
        return int(2*key+2)

    def swap(self,p1,p2):
        temp=self.heap[p1]
        self.heap[p1]=self.heap[p2]
        self.heap[p2]=temp

    def insertKey(self,value):
        i=deepcopy(self.heap_size)
        self.heap.append(value)
        self.heap_size+=1

        while i!=0 and self.heap[self.parent(i)]<self.heap[i]:
            self.swap(self.parent(i),i)
            i=self.parent(i)
    def maxHeapify(self,key,size):
        l=self.left(key)
        r=self.right(key)

        smallest=deepcopy(key)

        if l<size and self.heap[l]>self.heap[smallest]:
            smallest=l
        
        if r<size and self.heap[r]>self.heap[smallest]:
            smallest=r

        if smallest!=key:
            self.swap(smallest,key)
            self.maxHeapify(smallest,size)
    
    def heap_sort(self):
        if len(self.heap)==0:
            return "Bad Heap"
        if len(self.heap)==1:
            return self.heap
        size=deepcopy(self.heap_size)
        while size!=0:
            self.swap(0,size-1)
            size-=1
            self.maxHeapify(0,size)
if __name__=="__main__":
    h=Heap(6)
    h.insertKey(3)
    h.insertKey(2)
    h.insertKey(15)
    h.insertKey(5)
    h.insertKey(4)
    h.insertKey(45)
    print(h.heap)
    h.heap_sort()
    print(h.heap)
