from copy import deepcopy
class Max_Heap:
    def __init__(self,n):
        self.heap_array=[]
        self.capacity=n
        self.current_heap_size=0

    def parent(self,key):
        return int((key-1)/2)
    
    def left(self,key):
        return int(2*key+1)
    
    def right(self,key):
        return int(2*key+2)
    
    def swap(self,a,b):
        temp=self.heap_array[a]
        self.heap_array[a]=self.heap_array[b]
        self.heap_array[b]=temp
    
    def insertKey(self,key):
        i=deepcopy(self.current_heap_size)
        self.heap_array.append(key)
        self.current_heap_size+=1
        while i!=0 and self.heap_array[i]>self.heap_array[self.parent(i)]:
            self.swap(i,self.parent(i))
            i=self.parent(i)

    def maxHeapify(self,key):
        l=self.left(key)
        r=self.right(key)

        smallest=deepcopy(key)

        if l<self.current_heap_size and self.heap_array[l]>self.heap_array[smallest]:
            smallest=l
        
        if r<self.current_heap_size and self.heap_array[r]>self.heap_array[smallest]:
            smallest=r
        
        if smallest!=key:
            self.swap(key,smallest)
            self.maxHeapify(smallest)

    def increaseKey(self,key,new_value):
        self.heap_array[key]=new_value
        self.maxHeapify(0)

    def decreaseKey(self,key,new_value):
        self.heap_array[key]=new_value
        print("Delete",self.heap_array)
        # while (key != 0 and self.heap_array[key] > self.heap_array[self.parent(key)]): 
        #     self.swap(key, self.parent(key))
            
        #     key = self.parent(key)
        #self.maxHeapify(0)
        
        
        
        

    def deleteKey(self,key):
        self.decreaseKey(key,float("inf"))
        self.extractMin()
        

    def changeValue(self,key,new_value):
        if self.heap_array[key]==new_value:
            return
        if new_value<self.heap_array[key]:
            self.increaseKey(key,new_value)
        else:
            self.decreaseKey(key,new_value)
        

    def extractMin(self):
        if self.current_heap_size==0:
            return float("inf")
        if self.current_heap_size==1:
            return self.heap_array[0]

        root=self.heap_array[0]
        self.swap(0,self.current_heap_size-1)
        #self.heap_array[0]=self.heap_array[self.current_heap_size-1]
        self.current_heap_size-=1
        self.maxHeapify(0)
       
        return root


    

if __name__=="__main__":
    h=Max_Heap(6)
    h.insertKey(3)
    h.insertKey(2)
    h.insertKey(15)
    h.insertKey(5)
    h.insertKey(4)
    h.insertKey(45)
    print(h.heap_array)
    # print(h.heap_array)
    # for i in range(6):
    #     val=h.extractMin()
    # print(h.heap_array)
    h.deleteKey(5)
    print(h.heap_array)
