# OOP Python

## What is OOP?

Object Oriented Programming (OOP) is a programming model that organizes software design around data/ objects, rather than functions and logic. The structure includes:

- Class: code written that acts as blueprint for individual objects, properties and methods 
- Objects: Thing you want to store and process data about.
- Methods/Operations - Functions that are defined inside a class that describe the behaviors of an object.​
- Properties/Attributes -  Defined in the class template and represent the state of an object.

## Human Example

![Screenshot 2022-08-04 at 15 58 04](https://user-images.githubusercontent.com/102330725/182879693-8e591da7-6a7d-4d0b-8235-c822298cc213.png)

### Step 1
```python
# create a Human class
class Human:
    # __init__ to declare class attributes
    def __init__(self): # self refers current class
        self.eyes = 2
        self.hand = 2
        self.nose = True

    def eat(self):
        return "Eat three healthy meals everyday!"

    def move(self):
        return "Move, exercise, play. Stay fit"

    def sleep(self):
        return "Happy humans sleep 8 hours a day"

# create an object of the class before using it
human_object = Human()

print(human_object.nose)
print(human_object.sleep()) #abstraction
```

### Step 2
```python
# import parent class
from human import Human

#create a child class
class Male(Human):

    def __init__(self):
        # let it know to inherit everything from parent class
        super().__init__() # super is used to inherit everything from base class
        self.beard = True
        self.height = 7
        self.hobby = "gardening"

    def run(self):
        return "Males run at an average speed of 8 mph"

    def talk(self):
        return "Most common talk is sports and gym"

    def swim(self):
        return "Swimming can improve exercise-induced asthma"

male_object = Male()
print(male_object.beard)
print(male_object.talk())
```

### Step 3

```python
from male import Male

class Boy(Male):

    def __init__(self):
        super().__init__()
        self.beard = False # polymorphism
        self.height = 4
        self.hand = "small"

    def play(self):
        return "Kids love to play"

    def run(self):
        return "Running is also a good exercise"

    def laugh(self):
        return "laugh till your stomach hurts"

boy_object = Boy()
print(boy_object.beard)
print(boy_object.run())
```

### Step 4

```python
from human import Human

class Female(Human):

    def __init__(self):
        super().__init__()
        self.fav_colour = "white"
        self.breathe = True
        self.hair = True

    def dance(self):
        return "You can learn to dance whether you have been born with natural talent or not."

    def code(self):
        return "Ada Lovelace is credited for being the world's first programmer"

    def drive(self):
        return "Enjoy driving"

female_object = Female()
print(female_object.hair)
print(female_object.code())
```

### Step 5

```python
from female import Female

class Girl(Female):
    def __init__(self):
        super().__init__()
        self.__fav_colour = "blue" # encapsulation __private
        self._nature = "happy" #_protected
        self.heart = 1

    def _study(self): # _protected function
        try:
            return girl_object._study()

        except RecursionError:
            return "this information is protected"

    def play(self):
        return "Play everyday"

    def paint(self):
        return "Love to paint"

girl_object = Girl()
print(girl_object._nature)
print(girl_object._study())
# print(girl_object.__fav_colour)
```
