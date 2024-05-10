class stack:
    def __init__(self):
        self.s=[]
        
    def is_empty(self):
        return len(self.s)==0
        
    def push(self,data):
        self.s.append(data)
        
    def pop(self):
        if not self.is_empty() : 
            return self.s.pop()
        else:
            raise IndexError("Stack is Empty")
             
    def peek(self):
        if not self.is_empty():
            return self.s[-1]
        else:
            raise IndexError("Stack is Empty")
            
    def size(self):
        return len(self.s)       
            
s=stack()
s.push(2)
s.push(3)
s.push(4)
print("Top:",s.peek())
print("Remove:",s.pop())
print("Top:",s.peek())
print("Size:",s.size())

            
            
            