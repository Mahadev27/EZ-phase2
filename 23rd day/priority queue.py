students_grade=[]
students_grade.append((4,'Mahadev'))
students_grade.append((1,'Chintu'))
students_grade.append((2,'Sindhu'))
students_grade.append((3,'Manisha'))
students_grade.sort(reverse=True)
print("Priority Queue:\n")
print(students_grade)
print("Original Queue:\n")
while students_grade:
    print(students_grade.pop())
