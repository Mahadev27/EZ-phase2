l1=[]
def insert(x):
    for i in range(0,x):
       a=int(input("Insert a number:"))
       l1.append(a)
    switch()
def delete(x):
    a=int(input("Enter the item to delete:"))
    if a in l1:
        l1.remove(a)
        print("Deletion Successful")
    else:
        print("Element is not found")
    switch()
def search():
    s=int(input("Enter the search element:"))
    found=0
    for i in range(len(l1)):
        if s==l1[i]:
            found=1
    if found==1:
        print('Element is found')
    else:
        print('Element is not found')
    switch()
def sort():
    l1.sort()
    print("Element is sorted")
    switch()
def display():
    print(l1)
    switch()
def switch():
    print("1.Insert")
    print("2.Delete")
    print("3.Search")
    print("4.Sort")
    print("5.Display")
    opt=input("Enter a option:")
    if opt=='1':
        global x
        x=int(input("Enter the size of the array:"))
        insert(x)
    elif opt=='2':
        delete(x)
    elif opt=='3':
        search()
    elif opt=='4':
        sort()
    elif opt=='5':
        display()
    else:
        print('Invalid option')
switch()