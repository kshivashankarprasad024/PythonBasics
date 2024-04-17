class card:
    def __init__(self,cimageurl,cprice,cratings,cdescription,cdelivery,ccomments,cbrandname):
        self.imageURL=cimageurl
        self.price=cprice
        self.ratings=cratings
        self.description=cdescription
        self.delivery=cdelivery
        self.comments=ccomments
        self.brandname=cbrandname

laptop=card("dummy url-1",45000,4.5,"best for student use","20th april 2024",["fantastic","superb","lovely","bad"],"maja")
print(laptop.imageURL)
print(laptop.price,end="  ")
print(laptop.ratings,end="  ")
print(laptop.description,end="  ")
print(laptop.delivery,end="  ")
print(laptop.comments,end="  ")
print(laptop.brandname)

mobile=card("dummy url-2",25000,3.5,"best device","20th april 2024",["fantastic","superb","lovely","bad","disapointed"],"jockey")
print(mobile.imageURL)
print(mobile.price,end="  ")
print(mobile.ratings,end="  ")
print(mobile.description,end="  ")
print(mobile.delivery,end="  ")
print(mobile.comments,end="  ")
print(mobile.brandname)

watch=card("dummy url-3",5000,4,"high performance","20th april 2024",["fantastic","superb","lovely","bad","disapointed"],"yoo")
print(watch.imageURL)
print(watch.price,end="  ")
print(watch.ratings,end="  ")
print(watch.description,end="  ")
print(watch.delivery,end="  ")
print(watch.comments,end="  ")
print(watch.brandname)
