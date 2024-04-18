class box:
    def __init__(self,name,rollno):
        self.name=name
        self.rollno=rollno
class box2(box):
    def __init__(self,marks,name,rollno):
        self.marks=marks
        box.__init__(self,name,rollno)



obj123=box2(1,"shiva",24)
print(obj123.name)
print(obj123.marks)
print(obj123.rollno)
