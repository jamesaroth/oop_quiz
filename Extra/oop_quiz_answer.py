
class Animal:
    def __init__(self, name):
        self.species = "no species specified"
        self.name = name
    
    def __str__(self):
        return "{}, species: {}".format(self.name, self.species)
    
    def make_noise(self):
        return "\n"
    
class Tiger(Animal):
    def __init__(self, name):
        super().__init__(self)
        self.name = name
        self.species = "tiger"
    
    def make_noise(self):
        return "Roar!"

class Dog(Animal):
    def __init__(self, name):
        super().__init__(self)
        self.name = name
        self.species = "dog"
    
    def make_noise(self):
        return "Bark!"

class Cow(Animal):
    def __init__(self, name):
        super().__init__(self)
        self.name = name
        self.species = "cow"
    
    def make_noise(self):
        return "Moo!"

class Zoo:
    def __init__(self):
        self.animal_list = []
    
    def add(self, animal):
        self.animal_list.append(animal)
    
    def show_animals(self):
        for i in self.animal_list:
            print("{}\n{}".format(i, i.make_noise()))


mike = Tiger("Mike")
molly = Dog("Molly")
bessie = Cow("Bessie")

zoo = Zoo()
zoo.add(mike)
zoo.add(molly)
zoo.add(bessie)      
zoo.show_animals()


