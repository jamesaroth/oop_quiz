## Classes & Objects Quiz

### Animal classes

Create the following classes:

Animal

Animal has a property called "species" and a property called "name". "species" is initialized to "no species specified", "name" is set by an argument to the constructor.

```
mike = Animal("Mike")
mike.species # "no species specified"
mike.name    # Mike
```

Give animal a meaningful string conversion that displays its name & species.

```
print(mike)

Mike, the no species specified.
```

Animal also has a method called "make_noise()" that prints out a blank line.

```
mike.make_noise()
                    # blank line printed
```

### Animal subclasses

Create the following subclasses of Animal:

* Tiger

Tiger's species property is "tiger" and its "make_noise()" method prints out "Roar!"

* Dog

Dog's species property is "dog" and its "make_noise()" method prints out "Bark!"

* Cow

Cow' species property is "cow" and its "make_noise()" method prints out "Moo!"

Each of the subclasses should set their name property using Animal's initializer
(that is, you should use `super()`)

### Zoo class

Now create a class called Zoo. It has a property called "animals" that is initialized to a blank list

Zoo has a method called "add(animal)" that appends an instance of Animal or one of its subclasses to the animals list.

Zoo has a method called "show_animals()." For each animal in the animals property, print that animal's string representation and then call its "make_noise" method.

```
mike = Tiger("Mike")
molly = Dog("Molly")
bessie = Cow("Bessie")

zoo = Zoo()
zoo.add(mike)
zoo.add(molly)
zoo.add(bessie)

zoo.show_animals()
Mike the tiger
Roar!
Molly the dog
Bark!
Bessie the cow
Moo!
```

Bonus: can you use `isinstance()` to make Zoo raise an error if you attempt to
`.add()` a value that is not an Animal or a subclass of Animal, it raises an
exception?
