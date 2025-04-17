'''
#initiate a class
class employee:
    #special method/magic method/dunder method - constructor
    def __init__(self) : 
        print("Started executed attributes/data")
        self.id = 123
        self.salary = 50000
        self.designation = "SDE"
        print("attributes/data has been initiated")

    def travel(self, destinataion):
        print("This travel method was called manually")
        print(f"Employee is now travelling to {destinataion}")


#create an obj/instance of the class

sam = employee()
print(sam.salary) 
print(sam.id)
sam.travel("Bangladesh")


print(type(sam))'''

a = 'x'
b = 'y'
print(a+b)
