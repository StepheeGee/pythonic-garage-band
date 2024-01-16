# LAB - Class 04

## Project: Pythonic Garage Band

**Author:** Stephanie G Johnson

**Description:**

This project explores object-oriented programming concepts in Python by creating a simulation of a garage band. It uses classes to model musicians, bands, and their interactions.

**Features:**

* Create instances of musicians (guitarists, bassists, drummers) with their names and instruments
* Form bands with different lineups of musicians
* Simulate band performances by calling the `play_solos()` method on a band instance
* Keep track of all created bands using the `Band.to_list()` method

**Links and Resources:**

[Code](pythonic_garage_band/garage_band.py)

**Setup:**

1. Clone this repository
2. Navigate to the project directory in your terminal
3. Run the program using `python garage_band.py`

**Usage:**

1. Create musicians:

   ```python
   guitarist = Guitarist("Jimi Hendrix")
   bassist = Bassist("Paul McCartney")
   drummer = Drummer("John Bonham")


2. Create a band:

```python
band = Band("The Power Trio", [guitarist, bassist, drummer])
```

3. Make the band play solos:

   ```python
   print(band.play_solos())
   ```

**Tests:**

* The project includes a suite of automated tests using the pytest framework. These tests cover various aspects of the code, including:
    * Correct behavior of `str()` and `repr()` methods for musicians
    * Functionality of band creation and management
    * Solo-playing capabilities of musicians
    * Tracking of created bands

**To run the tests:**

1. Navigate to the project directory in your terminal
2. Run the command `pytest`

**Additional Notes:**

* Consider adding user interface elements for band creation and editing (stretch goal).
* Explore adding more musician types and features to expand the simulation (stretch goal).
* The `clean()` function can be used to reset the list of created bands.

**Python Code Structure:**

The project's code is organized in the following files:

* `garage_band.py`: Contains the core classes and functions for musicians and bands.
* `test_garage_band.py`: Implements the tests using pytest.

**ChatGPT Notes*:**

In object-oriented programming, a class is a blueprint for creating objects, and an instance is a specific object created from that blueprint. Let's break down the provided code to understand the difference:

### Class Definition (e.g., `Musician`):

A class is a template or blueprint that defines the structure and behavior of objects. In your code:

```python
class Musician:
    # Class variable shared by all instances
    members = []

    def __init__(self, role, instrument, name):
        # Instance variables specific to each object
        self.role = role
        self.instrument = instrument
        self.name = name
        self.__class__.members.append(self)
```

- **Class (`Musician`) Definition:**
  - Contains methods and attributes shared by all instances.
  - `members` is a class variable shared by all instances.

### Instance Creation (e.g., `guitarist_instance`):

An instance is a specific object created from a class, following the blueprint. In your code:

```python
guitarist_instance = Guitarist("John")
```

- **Instance (`guitarist_instance`) Creation:**
  - An object of the `Guitarist` class.
  - Inherits attributes and methods from the `Musician` class due to inheritance.

### Inheritance (e.g., `Guitarist`, `Bassist`, `Drummer`):

Inheritance allows a new class (`Guitarist`, `Bassist`, `Drummer`) to inherit attributes and methods from an existing class (`Musician`). For example:

```python
class Guitarist(Musician):
    # Additional methods or attributes specific to Guitarist
    def __init__(self, name):
        super().__init__("Guitarist", "guitar", name)
        self.name = name
```

- `Guitarist` is a subclass of `Musician`.
- Inherits attributes and methods from `Musician` using `super()`.

### Object Instantiation:

Creating instances of classes (e.g., `Guitarist("John")`, `Bassist("Mike")`) creates specific objects with unique attribute values but shares common methods and class variables.

### Class (`Band`) and Class Methods:

```python
class Band:
    instances = []

    def __init__(self, name, members=None):
        # Instance variables specific to each Band object
        self.name = name
        self.members = members or []
        self.__class__.instances.append(self)

    @classmethod
    def to_list(cls):
        # Class method operates on the class itself
        return Band.instances
```

- `Band` is another class that represents a musical band.
- `to_list()` is a class method that operates on the class rather than an instance.

In summary, a class defines a blueprint, and an instance is a specific object created from that blueprint. Instances can have unique attribute values while sharing common methods and class variables with other instances of the same class.

