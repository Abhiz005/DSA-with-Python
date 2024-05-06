class Node:
    def __init__(self,data=None,next=None):
        self.data=data
        self.next=next

class CLL:
    def __init__(self,last=None):
        self.last=last

    def is_empty(self):
        return self.last is None

    def insert_at_start(self,data):
        n=Node(data)
        if self.last is None:
            n.next=n
            self.last=n
        else:
            n.next=self.last.next
            self.last.next=n

    def insert_at_after(self,temp,data):
        if temp is not None:
            n=Node(data,temp.next)
            temp.next=n
            if temp==self.last:
                 self.last=n

    def insert_at_last(self,data):
        n=Node(data)
        if self.last is None:
            n.next=n
            self.last=n
        else:
            n.next=self.last.next
            self.last.next=n
            self.last=n
    
    def search(self,data):
        if self.last is not None:
            temp=self.last.next
            while temp!=self.last:
                if temp.data==data:
                    return temp
                temp=temp.next
            if temp.data==data:
                return temp
            return None
        
    def del_at_first(self):
        if self.last is not None:
            if self.last.next==self.last:
                self.last=None
            else:
                self.last.next=self.last.next.next


    def del_at_item(self,data):
        if self.last  is not None:
            if self.last.next==self.last:
                if self.last.data==self.data:
                    self.last=None
            else:
                if self.last.next.data==data:
                    self.del_at_first()
                else:
                    temp=self.last.next
                    while temp!=self.last:
                        if temp.next==self.last:
                            if self.last.data==data:
                                self.del_at_last()
                                break
                        if temp.next.data==data:
                            temp.next=temp.next.next
                            break
                        temp=temp.next


    def del_at_last(self):
        if self.last is not None:
            if self.last.next==self.last:
                self.last=None
            else:
                temp=self.last.next
                while temp.next!=self.last:
                    temp=temp.next
                temp.next=self.last.next
                self.last=temp

       
    def display(self):
        if self.last is not None:
            temp=self.last.next
            while temp!=self.last:
                print(temp.data)
                temp=temp.next
            print(temp.data)


c=CLL()
print(c.is_empty())
c.insert_at_start(3)
c.insert_at_start(2)
c.insert_at_after(c.search(2),5)
c.insert_at_last(10)
c.display()
print(c.search(20))
print("After delete:")
c.del_at_first()
c.del_at_last()
c.del_at_item(3)
c.display()