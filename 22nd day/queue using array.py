queue=[]
def Enqueue():
    item=int(input("Enter item:"))
    queue.append(item)
def Dequeue():
    if not queue:
        print("Queue is empty")
    else:
        a=queue.pop(0)
        print("Removed Element:",a)
def display():
    if not queue:
        print("Queue is empty")
    else:
        for i in range(0,len(queue)):
            print(queue[i],end="|")
while True:
    print("\n1.Enqueue\n2.Dequeue\n3.Display\n4.Quit")
    choice=int(input("Enter choice:"))
    if choice==1:
        Enqueue()
    elif choice==2:
        Dequeue()
    elif choice==3:
        display()
    elif choice==4:
        break
    else:
        print("Invalid Choice")
    
