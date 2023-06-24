r=int(input("Enter number of rows"))
c=int(input("Enter number of coloumns"))
matrix=[]
for i in range(r):
    a=[]
    for j in range(c):
        x=int(input("Enter the item"))
        a.append(x)
    matrix.append(a)
print("first matrix")
for i in range(r):
    for j in range(c):
        print(matrix[i][j],end=' ')
    print()
matrix1=[]
for i in range(r):
    b=[]
    for j in range(c):
        y=int(input("Enter the item"))
        b.append(y)
    matrix1.append(b)
print("second matrix")
for i in range(r):
    for j in range(c):
        print(matrix1[i][j],end=' ')
    print()
print("addition matrix is:")    
for i in range(r):
    for j in range(c):
        print(matrix[i][j]+matrix1[i][j],end=' ')
    print()   
print("multiply matrix is:")    
for i in range(r):
    for j in range(c):
        print(matrix[i][j]*matrix1[i][j],end=' ')
    print()