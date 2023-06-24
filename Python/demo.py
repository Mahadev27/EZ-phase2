class Student:
    M=99
    P=90
    C=87
    def total(self):
        return(self.M + self.P+ self.C)
    def set_M(self,x):
        self.M=x
ram=Student()
ram.M+=5
print(ram.total())
sindhu=Student()
sindhu.set_M(80)
print(sindhu.total())
