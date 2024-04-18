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



obj123=box3(60000,"shiva",24,100)
print(obj123.name)
print(obj123.marks)
print(obj123.rollno)
print(obj123.fees)



