class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class CLL:
    def __init__(self):
        self.head=None
    def insert_begining(self,data):
        nb=Node(data)
        nb.next=self.head
        self.head=nb
    def insert_ending(self,data):
        nb=Node(data)
        temp=self.head
        while temp.next!=None:
            temp=temp.next
        temp.next=nb
        nb.next=None
    def insert_position(self,data):
        np=Node(data)
        temp=self.head
        loc=int(input("Enter position:"))
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
            if temp==None:
                print("Location is not found")
            else:
                ptr.next=np
                np.next=temp
    def display(self):
        if self.head is None:
            print("List is Empty")
        else:
            temp=self.head #temp=first node
            while temp:
                if temp.next!=None:
                    print(temp.data,end=" -> ")
                else:
                    print(temp.data,end=" ")
            #temp.data means first node's data
                temp=temp.next
obj=CLL()
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
        node.next=newnode
        newnode.next=obj.head
        node=newnode
        
obj.display()    
print(" ")
#obj.insert_begining(70)
#obj.insert_ending(60)
#obj.insert_position(80)
#obj.display()


class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class CLL:
    def __init__(self):
        self.head=None
    def insert_begining(self,data):
        nb=Node(data)
        nb.next=self.head
        self.head=nb
    def insert_ending(self,data):
        nb=Node(data)
        temp=self.head
        while temp.next!=None:
            temp=temp.next
        temp.next=nb
        nb.next=None
    def insert_position(self,data):
        np=Node(data)
        temp=self.head
        loc=int(input("Enter position:"))
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
            if temp==None:
                print("Location is not found")
            else:
                ptr.next=np
                np.next=temp
    def display(self):
        if self.head is None:
            print("List is Empty")
        else:
            temp=self.head #temp=first node
            while temp:
                if temp.next!=None:
                    print(temp.data,end=" -> ")
                else:
                    print(temp.data,end=" ")
            #temp.data means first node's data
                temp=temp.next
obj=CLL()
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
        node.next=newnode
        newnode.next=obj.head
        node=newnode
        
obj.display()    
print(" ")
#obj.insert_begining(70)
#obj.insert_ending(60)
#obj.insert_position(80)
#obj.display()