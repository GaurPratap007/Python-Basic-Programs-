#Python supports single, multiple, multilevel, hybrid and hierarchical inheritance
class Animal():
    def __init__(self):
        print("Animal Created")

    def eat(self):
        print("I am eating")

    def who_am_i(self):
        print("I am an animal")

class Dog(Animal):
    def __init__(self):
        Animal.__init__(self)
        print("Dog Created")
    def eat(self):
        Animal.eat(self)
        print("I like to eat dog food")
    def who_am_i(self):
        Animal.who_am_i(self)
        print("I am a dog to be specific")

dog1= Dog()
dog1.eat()
dog1.who_am_i()