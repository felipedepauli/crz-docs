class Test:
    pass # quando você quer que o python vá em frente sem reclamar da sintaxe

from datetime import datetime
import random

class Character:
    date_of_creation = int (datetime.strftime(datetime.now(), '%Y'))
    def __init__(self, nickname, name, surname, species, age, gender, eating=False, speaking=False):
        self.nickname   = nickname
        self.name       = name
        self.surname    = surname
        self.species    = species
        self.age        = age
        self.gender     = gender
        self.eating     = eating
        self.speaking   = speaking
        self.title      = "she" if gender == "female" else "he"
        
        self.greetings()
    
    def greetings(self):
        print(f'The character whom was created is {self.name.split()[0]}.\n{self.title.capitalize()} is a {self.species}. Do you like {self.species}s?\n{self.title.capitalize()} is {self.age} years old and right now {self.title} is {"" if self.speaking else "not "}speking.\n-------------------------')
        
    def speak(self):
        print("mmmam... I'm speaking!!!")

    def eat(self, comida):
        if (self.eating):
            print(f'{self.name} is eating {comida}. It looks delicious.')
        else:
            print(f'{self.name} is not eating {comida} because she is not eating.')

    def when_i_was_created(self):
        print(f'{self.name} was created in {self.date_of_creation}.')

    @classmethod
    def speaking(cls):
        print("Hi, I'm a speaking character.")

    @staticmethod
    def random_speaking():
        rand = random.randint(10000, 19999)
        print(rand)
        