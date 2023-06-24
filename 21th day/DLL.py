class Node:
    def __init__(self,data):
        self.data=data
        self.prev=None
        self.next=None
class DLL:
    def __init__(self):
        self.head=None
    def rotate(self):
        temp=self.head
        
    def display(self):
        if self.head is None:
            print("List is Empty")
        else:
            temp=self.head #temp=first node
            while temp:
                if temp.next!=None:
                    print(temp.data,end=" <--> ")
                else:
                    print(temp.data,end=" ")
            #temp.data means first node's data
                temp=temp.next
    def insert_begin(self,data):
        nb=Node(data)
        nb.next=self.head
        nb.previous=None
        self.head=nb        
    def insert_end(self,data):
        ne=Node(data)
        temp=self.head
        while temp.next!=None:
            temp=temp.next
        temp.next=ne
        ne.previous=temp
        ne.next=None 
    def insert_position(self,data):
        np=Node(data)
        temp=self.head
        loc=int(input("Enter location:"))
        c=1
        if loc==1:
            nb=Node(data)
            nb.next=self.head
            self.head=nb
        else:
            while temp!=None and c!=loc:
                ptr=temp
                c+=1
                temp=temp.next
            ptr.next=np
            temp.previous=np
            np.previous=ptr
            np.next=temp
    def delete_begin(self):        
        temp=self.head
        self.head=temp.next
        temp.next=None
        self.head.previous=None
        print("Deleted node is",temp.data)        
    def delete_end(self):
        temp=self.head
        while temp.next!=None:
            ptr=temp
            temp=temp.next
        ptr.next=None
        temp.previous=None
        print("Deleted node is",temp.data)
    def delete_position(self):        
        temp=self.head
        loc=int(input("Enter location:"))
        c=1
        while temp!=None and c!=loc:
            ptr=temp
            c+=1
            temp=temp.next
        if temp==None:
            print("location not found")
        else:
            print("deleted element:",temp.data)
            ptr.next=temp.next
            temp.next.previous=ptr
obj=DLL()
#Node creation - initialising
n=int(input("Enter no of nodes:"))
for i in range(1,n+1):
    if i==1:
        item=int(input("Enter item:"))
        node=Node(item)
        obj.head=node
    else:
        item=int(input("Enter item:"))
        newnode=Node(item)
        newnode.prev=node
        node.next=newnode
        node=newnode
obj.display()
print(" ")
obj.insert_begin(70)
obj.display()
print(" ")
obj.insert_end(60)
obj.display()
print(" ")
obj.insert_position(80)
obj.display()
print(" ")
print("Delete at begin:")
obj.delete_begin()
obj.display()
print(" ")
print("Delete at end:")
obj.delete_end()
obj.display()
print(" ")
print("Delete at position:")
obj.delete_position()
obj.display()