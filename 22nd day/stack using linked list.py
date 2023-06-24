class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class stack:
    def __init__(self):
        self.head=None
    def push(self,data):
        if self.head is None:
            self.head=Node(data)
        else:
            new_node=Node(data)
            new_node.next=self.head
            self.head=new_node
    def pop(self):
        if self.head is None:
            return None
        else:
            temp=self.head
            self.head=temp.next
            temp.next=None
            return temp.data
    def display(self):
        if self.head is None:
            print("Stack is Empty")
        else:
            temp=self.head #temp=first node
            while temp:
                print("|",temp.data,"|")
                temp=temp.next
obj=stack()
while True:
    print("1.Push\n2.Pop\n3.Display\n4.Peek\n5.Quit")
    choice=int(input("Enter choice:"))
    if choice==1:
        item=int(input("Enter item to push:"))
        obj.push(item)
    elif choice==2:
        popped=obj.pop()
        if popped==None:
            print("Stack is empty")
        else:
            print("Removed Element:",popped)
    elif choice==3:
        obj.display()
    elif choice==4:
        if obj.head==None:
            print("Stack is empty")
        else:
            print("Peek Element:",obj.head.data)
    elif choice==5:
        break
    else:
        print("Invalid Choice")