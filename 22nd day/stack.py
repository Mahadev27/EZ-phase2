stack=[]
def push():
    item=int(input("Enter item:"))
    stack.append(item)
def pop():
    if not stack:
        print("Stack is empty")
    else:
        a=stack.pop()
        print("Removed Element:",a)
def display():
    if not stack:
        print("stack is empty")
    else:
        for i in range(len(stack),0,-1):
            print("|",stack[i-1],"|")
def peek():
    if not stack:
        print("stack is empty")
    else:
        print("Peek Element:",stack[-1])
while True:
    print("1.Push\n2.Pop\n3.Display\n4.Peek\n5.Quit")
    choice=int(input("Enter choice:"))
    if choice==1:
        push()
    elif choice==2:
        pop()
    elif choice==3:
        display()
    elif choice==4:
        peek()
    elif choice==5:
        break
    else:
        print("Invalid Choice")
    