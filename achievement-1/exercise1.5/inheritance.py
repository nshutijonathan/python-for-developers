class Animal(object):
    # Every animal has an age, but a name may not be necessary
    def __init__(self, age):
        self.age = age
        self.name = None

    # We'll throw in getter methods for age and name
    def get_age(self):
        return self.age

    def get_name(self):
        return self.name

    # And setter methods as well
    def set_age(self, age):
        self.age = age

    def set_name(self, name):
        self.name = name

    # We'll also have a well-formatted string representation, too!
    def __str__(self):
        return str(self.age)


class Cat(Animal):
    # Introducing a new method where it speaks
    def speak(self):
        print("Meow")

    # Another neat string representation for cats
    def __str__(self):
        output = "\nClass: Cat\nName: " + str(self.name) + \
            "\nAge: " + str(self.age)
        return output


class Dog(Animal):
    # Implementing another speak() method for dogs
    def speak(self):
        print("Woof!")

    # String representation for dogs
    def __str__(self):
        output = "\nClass: Cat\nName: " + str(self.name) + \
            "\nAge: " + str(self.age)
        return output


a = Animal(2)
cat = Cat(2)
dog = Dog(6)
cat.set_name("Stripes")
dog.set_name("Bubbles")
cat.speak()
print(a)

print(dog)
