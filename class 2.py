class card:
    def __init__(self,cimageurl,cprice,cratings,cdescription,cdelivery,ccomments,cbrandname):
        self.imageURL=cimageurl
        self.price=cprice
        self.ratings=cratings
        self.description=cdescription
        self.delivery=cdelivery
        self.comments=ccomments
        self.brandname=cbrandname
    def printalldetails(self):
        print("product url is:",self.imageURL)
        print("product price is:",self.price)
        print("product rating is:",self.ratings)
        print("product description is:",self.description)
        print("product delivery is:",self.delivery)
        print("product comments is:",self.comments)
        print("product brandname is:",self.brandname)
print("maja brand new laptop details")       
laptop=card("dummy url-1",45000,4.5,"best for student use","20th april 2024",["fantastic","superb","lovely","bad"],"maja")
laptop.printalldetails()
print()
print("jockey brand new mobile details")
mobile=card("dummy url-2",25000,3.5,"best device","20th april 2024",["fantastic","superb","lovely","bad","disapointed"],"jockey")
mobile.printalldetails()
print()
print("yoo brand new watch details")
watch=card("dummy url-3",5000,4,"high performance","20th april 2024",["fantastic","superb","lovely","bad","disapointed"],"yoo")
watch.printalldetails()
