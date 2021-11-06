#Superclass: Animal
class Animal:
    species = None
    hunger = 50

    def __init__(self, name, species):
        self.name = name
        self.species = species

    def speak(self):
        print(f"Hey, I'm {self.name} the {self.species}!")

#Subclass: Cat
class Cat(Animal):

    def __init__(self, name, species="cat"):
        self.name = name
        self.species = species

    def greet(self):
        return "Meow!"

    def speak(self):
        print(f"Hey, I'm {self.name} the {self.species}!")

    def feed(self):
        print("Om nom nom!")


#Friendly Cat
class FriendlyCat(Cat):

    def greet(self):
        msg = super().greet()
        return f'{msg} You seem awesome.'

#Hungry Cat
class HungryCat(Cat):

    def greet(self):
        """Eats every time before it speaks."""

        self.feed()
        return super().greet()
