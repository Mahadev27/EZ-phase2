class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class LinkedList:
    def __init__(self):
        self.head=None
    def push(self,new_data):
        new_node=Node(new_data)
        new_node.next=self.head
        self.head=new_node
    def detectAndRemoveLoop(self):
        if self.head is None:
            return
        if self.head.next is None:
            return
        slow_p=self.head
        fast_p=self.head
        while(slow_p and fast_p and fast_p.next):
            slow_p=slow_p.next
            fast_p=fast_p.next.next
            if slow_p == fast_p:
                print("Meeting Point",slow_p.data)
                slow_p=self.head
                while(slow_p.next!=fast_p.next):
                    slow_p=slow_p.next
                    fast_p=fast_p.next
                print("Start of Loop",fast_p.next.data)
                fast_p.next=None
            
    def printList(self):
        temp=self.head
        while temp:
            print(temp.data,end="  ")
            temp=temp.next
Ilist=LinkedList()
Ilist.head=Node(50)
Ilist.head.next=Node(20)
Ilist.head.next.next=Node(15)
Ilist.head.next.next.next=Node(4)
Ilist.head.next.next.next.next=Node(10)
extra=Node(1)
Ilist.head.next.next.next.next.next=extra
extra.next=Ilist.head.next.next
Ilist.detectAndRemoveLoop()
print("Linked List after removing loop")
Ilist.printList()
