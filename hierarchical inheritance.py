class box:
    def __init__(self,name,rollno):
        self.name=name
        self.rollno=rollno
class box2:
    def __init__(self,marks):
        self.marks=marks
class box3(box,box2):
    def __init__(self,fees,name,rollno,marks):
        self.fees=fees
        box.__init__(self,name,rollno)
        box2.__init__(self,marks)
class box4(box3):
    def __init__(self,sem,name,rollno,marks,fees):
        self.sem=sem
        box3.__init__(self,name,rollno,marks,fees)



obj123=box4("2-1",155000,"shiva",24,100)
print(obj123.name)
print(obj123.rollno)
print(obj123.sem)
print(obj123.marks)
print(obj123.fees)




