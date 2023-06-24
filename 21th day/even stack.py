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
def evenstack():
    even=[]
    if not stack:
        print("stack is empty")
    else:
        for i in range(len(stack)):
            if stack[i]%2==0:
                even.append(stack[i])
        if not even:
            print("even stack is emptyt")
        else:
            for i in range(len(even),0,-1):
                print("|",even[i-1],"|")
def oddstack():
    odd=[]
    if not stack:
        print("stack is empty")
    else:
        for i in range(len(stack)):
            if stack[i]%2!=0:
                odd.append(stack[i])
        if not odd:
            print("Odd stack is emptyt")
        else:
            for i in range(len(odd),0,-1):
                print("|",odd[i-1],"|")
while True:
    print("\n1.Push\n2.Pop\n3.Display\n4.Even stack\n5.Odd stack\n6.Quit")
    choice=int(input("Enter choice:"))
    if choice==1:
        push()
    elif choice==2:
        pop()
    elif choice==3:
        display()        
    elif choice==4:
        evenstack()
    elif choice==5:
        oddstack()
    elif choice==6:
        break
    else:
        print("Invalid Choice")
    
