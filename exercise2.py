#Create a user class with properties i.e name,age,location.
class Employee:
    def __init__(self, name, age,location):
        self.name = name
        self.age = age
        self.location = location

E1 = Employee("Sandra", 25, "katwe")
print(E1.name)
print(E1.age)
print(E1.location)

#Create anew instance of the user class(anew object)
E2 = Employee("Rose", 30, "Makindye")
print(E2.name)
print(E2.age)
print(E2.location)

#Access the user's name and age
Employee = E1.name
Employee = E1.age

print(f"user's name:{E1.name}")
print(f"user's age:{E1.age}")

#Create afunction for the user class the prints a user's location
#print the user's location using this function.
def my_location(my):
    print("my_location:",my)
my_location("katwe")




