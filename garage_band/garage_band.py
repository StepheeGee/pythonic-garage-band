class Musician:
    def __init__(self, name, instrument):
        """
        Initialize a Musician.

        Parameters:
        - name (str): The name of the musician.
        - instrument (str): The musical instrument the musician plays.
        """
        self.name = name
        self.instrument = instrument

    def play(self):
        """
        Play the musician's instrument.

        Returns:
        str: A string indicating that the musician is playing their instrument.
        """
        return f"{self.name} is playing the {self.instrument}"

    def get_instrument(self):
        """
        Get the musician's instrument.

        Returns:
        str: The name of the instrument the musician plays.
        """
        return self.instrument

    def play_solo(self):
        """
        Play a solo.

        Raises:
        NotImplementedError: Subclasses must implement this method.
        """
        raise NotImplementedError("Subclasses must implement the play_solo method")

    def __str__(self):
        """
        Return a string representation of the musician.

        Returns:
        str: A string representation of the musician.
        """
        return f"{self.name} - {self.instrument}"

    def __repr__(self):
        """
        Return a string representation suitable for debugging.

        Returns:
        str: A string representation of the musician for debugging purposes.
        """
        return f"{self.__class__.__name__}('{self.name}')"


class Guitarist(Musician):
    def play_solo(self):
        """
        Play a guitar solo.

        Returns:
        str: A string indicating that the guitarist is playing a solo.
        """
        return f"{self.name} is playing an amazing guitar solo"


class Bassist(Musician):
    def play_solo(self):
        """
        Play a bass solo.

        Returns:
        str: A string indicating that the bassist is playing a solo.
        """
        return f"{self.name} is playing a groovy bass solo"


class Drummer(Musician):
    def play_solo(self):
        """
        Play a drum solo.

        Returns:
        str: A string indicating that the drummer is playing a solo.
        """
        return f"{self.name} is playing an energetic drum solo"


class Band:
    bands = []

    def __init__(self, name):
        """
        Initialize a Band.

        Parameters:
        - name (str): The name of the band.
        """
        self.name = name
        self.members = []
        Band.bands.append(self)

    def add_member(self, musician):
        """
        Add a musician to the band.

        Parameters:
        - musician (Musician): An instance of the Musician class.
        
        Raises:
        ValueError: If the given musician is not an instance of the Musician class.
        """
        if isinstance(musician, Musician):
            self.members.append(musician)
        else:
            raise ValueError("Invalid musician type")

    def play_solos(self):
        """
        Ask each member musician to play a solo in the order they were added to the band.

        Returns:
        list: A list of strings representing the solos played by each member.
        """
        solos = [member.play_solo() for member in self.members]
        return solos

    @classmethod
    def to_list(cls):
        """
        Get a list of previously created Band instances.

        Returns:
        list: A list of Band instances.
        """
        return cls.bands

    def __str__(self):
        """
        Return a string representation of the band.

        Returns:
        str: A string representation of the band.
        """
        return f"{self.name} - Members: {', '.join(str(member) for member in self.members)}"

    def __repr__(self):
        """
        Return a string representation suitable for debugging.

        Returns:
        str: A string representation of the band for debugging purposes.
        """
        return f"{self.__class__.__name__}('{self.name}')"



# Example usage:
if __name__ == "__main__":
    band1 = Band("Rock Band")
    guitarist1 = Guitarist("John")
    bassist1 = Bassist("Paul")
    drummer1 = Drummer("Ringo")

    band1.add_member(guitarist1)
    band1.add_member(bassist1)
    band1.add_member(drummer1)

    print(band1.play_solos())
    print(band1)

    print(Band.to_list())
