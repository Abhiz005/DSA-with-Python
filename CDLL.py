class Node:
    def __init__(self,prev=None,data=None,next=None):
        self.prev=prev
        self.data=data
        self.next=next

class CDLL:
    def __init__(self,start=None):
        self.start=start

    def is_empty(self):
        return self.start is None
    
    def insert_at_first(self,data):
        n=Node(data=data)
        if self.start is not None:
            n.prev=self.start.prev
            n.next=self.start
            self.start.prev.next=n
            self.start.prev=n
        else:
            n.prev=n
            n.next=n
        self.start=n
        
    def insert_after(self,temp,data):
        if temp is not None:
            n=Node(data=data)
            n.next=temp.next
            n.prev=temp
            temp.next.prev=n
            temp.next=n


    def insert_at_last(self,data):
        n=Node(data=data)
        if self.start is not None:
            n.prev=self.start.prev
            n.next=self.start
            n.prev.next=n
            self.start.prev=n
        else:
            n.prev=n
            n.next=n
            self.start=n
    
    def search(self,data):
        temp=self.start
        if temp==None:
            return None
        if temp.data==data:
            return temp
        else:
            temp=temp.next
            while temp!=self.start:
                if temp.data==data:
                    return temp
                temp=temp.next
            return None

    def display(self):
        if self.start is not None:
            temp=self.start
            while temp!=self.start.prev:
                print(temp.data,end=' ')
                temp=temp.next
            print(temp.data)

    def del_at_first(self):
        if self.start is not None:
            if self.start==self.start.next:
                self.start=None
            else:
                self.start.prev.next=self.start.next
                self.start.next.prev=self.start.prev
                self.start=self.start.next
                    
    def  del_at_last(self):
         if self.start is not None:
            if self.start==self.start.next:
                self.start=None
            else:
                self.start.prev.prev.next=self.start
                self.start.prev=self.start.prev.prev

    def del_item(self,data):
        if self.start is not None:
            temp=self.start
            if temp.data==data:
                self.del_at_first()
            else:
                temp=temp.next
                while temp  is not self.start:
                    if temp.data==data:
                        temp.next.prev=temp.prev
                        temp.prev.next=temp.next
                    temp=temp.next
            


d=CDLL()
print(d.is_empty())
d.insert_at_first(4)
d.insert_at_first(3)
d.insert_at_first(2)
d.insert_after(d.search(4),5)
d.insert_at_last(10)
d.display()
print("After DELETE")
d.del_at_first()
d.del_at_last()
d.del_item(4)
d.display()