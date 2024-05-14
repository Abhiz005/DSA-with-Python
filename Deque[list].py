class Deque:
    def __init__(self):
        self.s=[]
        
    def is_empty(self):
        return len(self.s)==0
            
    def insert_front(self,data):
        self.s.insert(0,data)
               
    def insert_rear(self,data):
        self.s.append(data)
        
    def delete_front(self):
        if not self.is_empty():
            self.s.pop(0)
        else: 
            raise IndexError ("Deque is empty ")
            
    def delete_rear(self):
        if not self.is_empty():
            self.s.pop()
        else: 
            raise IndexError ("Deque is empty ")              
    
    def get_front(self):
        if not self.is_empty():
            return self.s[0]
        else:
            raise IndexError ("Deque is empty")  
      
    def get_rear(self):
        if not self.is_empty():
            return self.s[-1]
        else:
            raise IndexError ("Deque is empty")  
        
    def size(self):
        return len(self.s)
        
q1=Deque()
try:
 print(q1.get_front())
except IndexError as e:
 print(e.args[0])
q1.insert_front (10)
q1.insert_front(20)
q1.insert_rear(30)
q1.insert_rear(40)
print("Front=",q1.get_front(), "Rear=",q1.get_rear())
try:
 q1.delete_rear()
 q1.delete_front()
 print("Queue has now", q1.size(),"elements")
except IndexError as e:
 print(e.args[0])
print("Front=",q1.get_front(), "Rear=",q1.get_rear())        
                