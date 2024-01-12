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

**Further Exploration:**

* Look into implementing user interfaces using frameworks like Qt or Tkinter.
* Consider incorporating song libraries and full song performances.
* Explore advanced object-oriented programming concepts like inheritance and polymorphism.

