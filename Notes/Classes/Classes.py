'''Classes 1 Lecture'''
# #Superclass: Animal
# class Animal:
#     species = None
#     hunger = 50

#     def __init__(self, name, species):
#         self.name = name
#         self.species = species

#     def speak(self):
#         print(f"Hey, I'm {self.name} the {self.species}!")

'''Classes 2 '''
# #Subclass: Cat
# class Cat(Animal):

#     def __init__(self, name, species="cat"):
#         self.name = name
#         self.species = species

#     def greet(self):
#         return "Meow!"

#     def speak(self):
#         print(f"Hey, I'm {self.name} the {self.species}!")

#     def feed(self):
#         print("Om nom nom!")


# #Friendly Cat
# class FriendlyCat(Cat):

#     def greet(self):
#         msg = super().greet()
#         return f'{msg} You seem awesome.'

# #Hungry Cat
# class HungryCat(Cat):

#     def greet(self):
#         """Eats every time before it speaks."""

#         self.feed()
#         return super().greet()

'''Classes 3'''

# Here is an example of a superclass Animal, and its subclasses Cat and Dog:

# class Animal:
#     def __init__(self, name, species):
#         self.name = name
#         self.species = species

#     def speak(self, greeting='Hey'):
#         print(f"{greeting}, I'm {self.name} the {self.species}")


# class Cat(Animal):
#     def __init__(self, name):
#         super().__init__(name, 'cat')

#     def speak(self):
#         super().speak('Meow')


# class Dog(Animal):
#     def __init__(self, name):
#         super().__init__(name, 'dog')

#     def speak(self):
#         super().speak('Woof')


# Animal is a base class, meaning we would never create an "Animal" instance,
# it is only meant to be inhereited from by subclasses.
# we can indicate to others that this class is non-functioning by giving it a
# name like "AbstractAnimal" ir "BaseAnimal"

# Since we know all animals will have a species and a greeting,
# Here is a simpler way to code the above:

# class BaseAnimal:
#     greeting = 'Hey!'
#     species = None

#     def __init__(self, name):
#         self.name = name

#     def speak(self):
#         print(f"{self.greeting}, I'm {self.name} the {self.species}")


# # class Cat(BaseAnimal):
# #     greeting = 'Meow'
# #     species = 'cat'


# # class Dog(BaseAnimal):
# #     greeting = 'Woof'
# #     species = 'dog'

# # notice that we do not need separate __init__ for the subclasses
# # because they use the they use the one in the superclass


# # If we want to supply a feature to a subclass without chasing the base
# # class (Animal), we can use a mixin:

# class ChaseLaserMixin:
#     """Can chase laser pointers."""

#     def chase_laser(self):
#         print('Wheee!')


# class HasFurMixin:
#     """Has fur."""

#     def enfur(self):
#         print('Fur everywhere!!')

# class Cat(ChaseLaserMixin, HasFurMixin, BaseAnimal):
#     greeting = 'Meow'
#     species = 'cat'

# class Dog(HasFurMixin, BaseAnimal):
#     greeting = 'Woof'
#     species = 'dog'

'''Classes 4'''

class Cat:
    greeting = 'Meow'
    species = 'cat'
    def __init__(self, name, hunger = 100):
        self.name = name
        self.hunger = hunger

    def speak(self):
        print(f"{self.greeting}, I'm {self.name} the {self.species}")

    def feed(self, calories):
        self.hunger = self.hunger - calories

    # def cat_food_to_calories(self, food_amt):
    #     """Convert an amount of cat food to calories"""
    #     return food_amt * 0.3456

# '''
# What if we want to convert cat food to calories without instantiating a cat first?
# We can make this a static method:
# '''

    @staticmethod
    def cat_food_to_calories(food_amt):
        """Convert an amount of cat food to calories"""
        return food_amt * 0.3456

# Notice that we no longer need "self" because this is no longer an instance method.

    @classmethod
    def from_file(cls, name):
        for line in open(cls._data_file):
            data_name, data_hunger = line.strip().split(',')

            if data_name == name:
                return cls(data_name, float(data_hunger))
