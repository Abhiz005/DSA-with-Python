class Node:
    def __init__(self,prev=None,data=None,next=None):
        self.prev=prev
        self.data=data
        self.next=next

class DLL:
    def __init__(self,start=None):
        self.start=start
    
    def is_empty(self):
        return self.start is None
    
    def insert_at_start(self,data):
        n=Node(None,data,self.start)
        if not self.is_empty():
            self.start.prev=n
        self.start=n

    def insert_at_middle(self,temp,data):
        if temp is not None:
            n=Node(temp,data,temp.next)
            if temp.next is not None:
                temp.next.prev=n
            temp.next=n


    def insert_at_last(self,data):
        temp=self.start
        if self.start is not None:
            while temp.next is not None:
                temp=temp.next
        n=Node(temp,data,None)
        if temp==None:
            self.start=n
        else:
            temp.next=n

   
    def search(self,data):
        temp=self.start
        while temp is not None:
            if temp.data==data:
                return temp
            temp=temp.next
        return None
    
    def display(self):
        temp=self.start
        while temp is not None:
            print(temp.data,end=' ')
            temp=temp.next

    
    def del_at_first(self):
        if self.start is not None:
            if self.start.next is None:
                self.start=None
            else:
                self.start.next.prev=None
                self.start=self.start.next

    
    def del_at_last(self):
        if self.start is not None:
            if self.start.next is None:
                self.start=None
            else:
                    temp=self.start
                    while temp.next is not None:
                        temp=temp.next
                    temp.prev.next=None

    def delete_item(self,data):
        if self.start.data is None:
            pass
        else:
            temp=self.start
            while temp is not None:
                if temp.data==data:
                    if temp.next is not None:
                        temp.next.prev==temp.prev
                    if temp.prev is not None:
                        temp.prev.next=temp.next
                    else:
                        self.start=temp.next
                    break
                temp=temp.next

                    



d=DLL()
print(d.is_empty())
d.insert_at_start(30)
d.insert_at_start(20)
d.insert_at_middle(d.search(20),40)
d.insert_at_last(50)
d.del_at_first()
d.delete_item(30)
d.del_at_last()
d.del_at_last()
d.del_at_last()
d.display()
print(d.search(20))
