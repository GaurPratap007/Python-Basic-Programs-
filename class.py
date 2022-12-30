#Declaring a class

# class dog():
#     def __init__(self, mybreed, name, age):
#         self.breed = mybreed
#         self.name = name
#         self.age = age

#     def bark(self):
#         print("WOOF! My name is {}".format(self.name))
# #Creating an instance
# my_dog = dog('Husky', 'Shiro', 5)
# print("Name of the Dog : ",my_dog.name, ", Breed of the Dog : ",my_dog.breed, ", Age of the Dog : ",my_dog.age)
# print(my_dog.bark())

class Circle():
    pi = 3.14

    def __init__(self, radius):
        self.radius = radius

    def get_circumference(self):
        return self.radius*Circle.pi*2
    
    def get_area(self):
        return self.radius*self.radius*Circle.pi

circle1 = Circle(10)
print(circle1.get_area())
print(circle1.get_circumference())

