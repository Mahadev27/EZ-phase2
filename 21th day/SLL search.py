class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class SLL:
    def __init__(self):
        self.head=None
    def search(self):
        temp=self.head
        se=int(input("Enter serach element:"))
        found=0
        while temp.next!=None:
            if se==temp.data:
                found=1
                break
            else:
                temp=temp.next
        if found==1:
            print("Element is found")
        else:
            print("Element is not found")
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
obj=SLL()
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
        node=newnode
obj.display()    
print(" ")
obj.search()

