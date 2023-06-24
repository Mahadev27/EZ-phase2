class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node

    def rotate(self, k):
        if k == 0 or self.head is None or self.head.next is None:
            return

        current = self.head
        count = 1
        while count < k and current:
            current = current.next
            count += 1

        if current is None:
            return

        kth_node = current
        while current.next:
            current = current.next

        current.next = self.head
        self.head = kth_node.next
        kth_node.next = None

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


# Example usage
linked_list = LinkedList()
linked_list.append(1)
linked_list.append(2)
linked_list.append(3)
linked_list.append(4)
linked_list.append(5)

print("Original linked list:")
linked_list.display()
k = 1  # Number of rotations
print("\nAfter Rotation linked list:")
linked_list.rotate(k)
linked_list.display()
