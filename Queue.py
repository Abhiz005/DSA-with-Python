class Queue:
    def __init__(self):
        self.s=[]
        self.front=None
        self.rear=None
        
    def is_empty(self):
        return len(self.s)==0
            
    def enqueue(self,data):
        self.s.append(data)
        
    def dequeue(self):
        if not self.is_empty():
            self.s.pop(0)
        else: 
            raise IndexError ("Queue is Underflow ")      
    
    def get_front(self):
        if not self.is_empty():
            return self.s[0]
        else:
            raise IndexError ("Queue is Underflow")  
      
    def get_rear(self):
        if not self.is_empty():
            return self.s[-1]
        else:
            raise IndexError ("Queue is Underflow ")  
        
    def size(self):
        return len(self.s)
        
q1=Queue()
try:
 print(q1.get_front())
except IndexError as e:
 print(e.args[0])
q1.enqueue (10)
q1.enqueue(20)
q1.enqueue(30)
q1.enqueue(40)
q1.enqueue(50)
print("Front=",q1.get_front(), "Rear=",q1.get_rear())
try:
 q1.dequeue()
 print("Queue has now", q1.size(),"elements")
except IndexError as e:
 print(e.args[0])
        
                