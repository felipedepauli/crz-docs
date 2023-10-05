class MyClassDoesNothing:
    """
    HELP ---------------------------------------------------
    ---- This class does absolutily nothing!
    ---- To see this messagem, you have to use help(object).
    --------------------------------------------------------
    """
    def __init__(self, name, middle_name, last_name, age):
        self.name = name
        self.middle_name = middle_name
        self.last_name = last_name
        self.age = age

person = MyClassDoesNothing("Felipe", "Camargo", "de Pauli", 38)

help(person)

print(person.name, person.middle_name, person.last_name, " is ", person.age, "years old.")
