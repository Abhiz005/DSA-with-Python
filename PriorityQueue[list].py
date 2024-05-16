class PriorityQueue:
    def __init__(self):
        self.l=[]
        
    def push(self,data,p):
        index=0
        while index!=len(self.l) and self.l[index][1]<=p:
            index+=1
        self.l.insert(index,(data,p))
        
    def pop(self):
        if self.l is None:
            raise IndexError ("Priority Queue is Empty")
        return self.l.pop(0)[0]
                
    def is_empty(self):
        return len(self.l)==0 
        
    def size(self):
        return len(self.l)     
        
p=PriorityQueue()
p.push(20,10)     
p.push(10,5)
p.push(5,2)
p.push(8,4)
while not p.is_empty():
    print(p.pop())
   
            
      
        