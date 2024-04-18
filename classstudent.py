class box:
    def __init__(self,cname,crollno,cdbmsmarks,cpythonmarks,ccmarks,cosmarks,ccnmarks):
        self.name=cname
        self.rollno=crollno
        self.dbmsmarks=cdbmsmarks
        self.pythonmarks=cpythonmarks
        self.cmarks=ccmarks
        self.osmarks=cosmarks
        self.cnmarks=ccnmarks
student1=box("Harika","5A1",78,67,77,89,46)
print(student1.name,end=" ")
print(student1.rollno,end=" ")
print(student1.dbmsmarks,end=" ")
print(student1.pythonmarks,end=" ")
print(student1.cmarks,end=" ")
print(student1.osmarks,end=" ")
print(student1.cnmarks)
student2=box("Swapna","5A2",38,65,97,59,41)
print(student2.name,end=" ")
print(student2.rollno,end=" ")
print(student2.dbmsmarks,end=" ")
print(student2.pythonmarks,end=" ")
print(student2.cmarks,end=" ")
print(student2.osmarks,end=" ")
print(student2.cnmarks)
student3=box("Sushma","5A3",88,95,47,89,31)
print(student3.name,end=" ")
print(student3.rollno,end=" ")
print(student3.dbmsmarks,end=" ")
print(student3.pythonmarks,end=" ")
print(student3.cmarks,end=" ")
print(student3.osmarks,end=" ")
print(student3.cnmarks)
