class Musician:
    members = []

    def __init__(self, role, instrument, name):
        self.role = role
        self.instrument = instrument
        self.name = name
        self.__class__.members.append(self)

    def __str__(self):
        return f'My name is {self.name} and I play {self.instrument}'

    def __repr__(self):
        return f'{self.role} instance. Name = {self.name}'

    def play_solo(self):
        return f'{self.name} is playing solo on the {self.instrument}'

    def get_instrument(self):
        return self.instrument


class Guitarist(Musician):
    def __init__(self, name):
        super().__init__("Guitarist", "guitar", name)
        self.name = name

    def play_solo(self):
        return "face melting guitar solo"


class Bassist(Musician):
    def __init__(self, name):
        super().__init__("Bassist", "bass", name)
        self.name = name

    def play_solo(self):
        return "bom bom buh bom"


class Drummer(Musician):
    def __init__(self, name):
        super().__init__("Drummer", "drums", name)
        self.name = name

    def play_solo(self):
        return "rattle boom crash"


class Band:
    instances = []

    def __init__(self, name, members=None):
        self.name = name
        self.members = members or []
        self.__class__.instances.append(self)

    def play_solos(self):
        return [member.play_solo() for member in self.members]

    def __str__(self):
        return f"This is the {self.name}"

    def __repr__(self):
        return f"Band instance. Name = {self.name}"  

    @classmethod
    def to_list(cls):
        """
        I want a list of all the bands in the Band class.
        
        """
        return Band.instances


def clean():
    Band.instances = []
