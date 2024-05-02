class Node:
    def __init__(self,data=None,next=None):
        self.data=data
        self.next=next

class SLL:
    def __init__(self,start=None):
        self.start=start

    def is_empty(self):
        if self.start==None:
            return True
        else:
            return False

    def insert_at_first(self,data):
        n=Node(data,self.start)
        self.start=n

    def insert_at_middle(self,data,p):
        if self.is_empty==True:
            print("List is empty")
        else:
            temp=self.start
            while temp is not None:
                if temp.data==p:
                    n=Node(data,temp.next)
                    temp.next=n
                    break
                else:
                    print("NOT FOUND",p,"data in the middle of the Linked List")
                temp=temp.next
                
    def insert_at_last(self,data):
        n=Node(data)
        temp=self.start
        while temp.next is not None:
            temp=temp.next
        temp.next=n

    def search(self,s):
        temp=self.start
        while temp is not None:
            if temp.data==s:
                print("DATA FOUNDED:",s)
                break
            if temp.next==None:
                print("NOT FOUND:",s)
            temp=temp.next    
                    

    def display(self):
       temp=self.start
       if self.start is None:
            print("List is empty")
       else:
            while temp is not None:
                print(temp.data)
                temp=temp.next

    def delete_first(self):
        self.start=self.start.next

    def delete_last(self):
        temp=self.start
        while temp.next.next is not None:
            temp=temp.next
        temp.next=None

    def delete_item(self, d):
        temp = self.start
        while temp is not None:
            temp1 = temp.next
            if temp1 is not None and temp1.data == d:
                temp.next = temp1.next
                print("Element deleted successfully:", d)
            temp = temp.next


a=SLL()
print(a.is_empty())
a.insert_at_first(5)
a.insert_at_first(2)
a.insert_at_middle(3,2)
a.insert_at_last(10)
a.insert_at_last(12)
a.display()
a.search(5)
a.search(1)
a.delete_first()
a.delete_last()
a.display()
a.delete_item(5)
a.display()

