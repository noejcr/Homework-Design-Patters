#AbstractFactoryPattern.py

class Dog:
    """A simple dog class"""
    def speak(self):
        return "Woof!"
    def __str__(self):
        return "Dog"

class Cat:
    """A simple dog class"""
    def speak(self):
        return "Meow!"
    def __str__(self):
        return "Dog"

class Duck:
    """A simple duck class"""
    def speak(self):
        return "Quack!"
    def __str__(self):
        return "Duck"

class DogFactory:
    """Concete factory"""
    def get_pet(self):
        """Return a dog object"""
        return Dog()
    def get_food(self):
        """Return a dog food"""
        return "DogChow"

class CatFactory:
    """Concete factory"""
    def get_pet(self):
        """Return a cat object"""
        return Cat()
    def get_food(self):
        """Return a dog food"""
        return "Wiskas"

class DuckFactory:
    """Concete factory"""
    def get_pet(self):
        """Return a duck object"""
        return Duck()
    def get_food(self):
        """Return a duck food"""
        return "duck food"

class PetStore:
    """PetStore houses our abstract factory"""
    def __init__(self,pet_factory=None):
        """pet factory is our abstract factory"""
        self._pet_factory=pet_factory
    def show_pet(self):
        """Utility method to display the details of the objects returned by the factory"""
        pet=self._pet_factory.get_pet()
        pet_food=self._pet_factory.get_food()
        print("our pet is: '{}'".format(pet))
        print("our pet say hello by '{}'".format(pet.speak()))
        print("Its food is '{}'".format(pet_food))
    def set_factory(self, pet_factory):
        self._pet_factory=pet_factory
    

#Create a concrete factory
dog_factory=DogFactory()
#Create a pet store housing our abstract factory
shop=PetStore(dog_factory)
shop.show_pet()

#create a cat factory
cat_factory=CatFactory()
shop.set_factory(cat_factory)
shop.show_pet()

#create a duck factory
duck_factory=DuckFactory()
shop.set_factory(duck_factory)
shop.show_pet()
