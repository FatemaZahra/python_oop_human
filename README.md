# OOP Python

## What is OOP?

Object Oriented Programming (OOP) is a programming model that organizes software design around data/ objects, rather than functions and logic. The structure includes:

- **Class:** code written that acts as blueprint for individual objects, properties and methods 
- **Objects:** Thing you want to store and process data about.
- **Methods/Operations:** Functions that are defined inside a class that describe the behaviors of an object.​
- **Properties/Attributes:**  Defined in the class template and represent the state of an object.

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

## Four pillars of OOP

### Abstraction

It shows what is essential and hides what is unnecessary for the user to see. Gives us the ability to utilise something without fully understanding its functionality. 

![Screenshot 2022-08-05 at 08 46 22](https://user-images.githubusercontent.com/102330725/183028406-7e7dc9c2-6181-4266-a33e-3cd332334891.png)

### Encapsulation

It restricts access of variables and methods which prevents accidental modification
- Public: Accsessible within or outside a class
- Protected: Accessible within the class and its sub-classes
- Private: Accessible only within a class

![Screenshot 2022-08-05 at 08 47 32](https://user-images.githubusercontent.com/102330725/183028668-00d9ad4c-34d4-430a-abb2-c101ece1403d.png)

### Inheritance

- Inheritance refers to defining a new class with little or no modification to an existing class.
- The new class is called derived (or child) class and the one from which it inherits is called the base (or parent) class.
 
![Screenshot 2022-08-05 at 08 48 21](https://user-images.githubusercontent.com/102330725/183028831-df568ae7-5eef-4cc7-b4a6-8642b491257e.png)

### Polymorphism

The condition of occurrence in several different shapes/forms.


![Screenshot 2022-08-05 at 08 51 13](https://user-images.githubusercontent.com/102330725/183029320-6dd2b569-99c1-4fdd-bc7e-4bf3d203fb11.png)


![Screenshot 2022-08-05 at 08 51 44](https://user-images.githubusercontent.com/102330725/183029400-ebdc3ea9-1908-42ca-bf87-c2366b686a13.png)

### Keywords explained

- **super():** The super() function is used to give access to methods and properties of a parent or sibling class. The super() function returns an object that represents the parent class.

- **init():** The __init__ function is called every time an object is created from a class. The __init__ method lets the class initialize the object's attributes and serves no other purpose. It is only used within classes

- **pass:** accept the default parent methods
