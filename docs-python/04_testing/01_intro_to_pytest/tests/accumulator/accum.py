# ----------------------------------------------------
# Class: Accumulator
# ----------------------------------------------------

class Accumulator:
    def __init__(self):
        self._count = 0

    def add(self, more=1):
        if more < 0:
            raise ValueError("Can't add a negative number")
        self._count+= more

    @property
    def count(self):
        return self._count