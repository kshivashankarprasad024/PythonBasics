class block:
    def __init__(self,identity,proof):
         self.identity=identity
         self.proof=proof
    def student(self):
        print("hi hello")
        print("i am student")
    def teacher(self):
        print("good morning")
        print("i am teacher")
    def myself(self):
        print("i am student")
        print("from nitm")
obj123=block(14,56)
obj123.student()
obj121=block(89,52)
obj121.teacher()
obj122=block(56,89)
obj122.myself()
