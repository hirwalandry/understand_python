class Person:
    def __init__(self, name):
        self.name = name
    def talk(self):
        return f"I am {self.name} "

person_One = Person("Landry")
print(person_One.talk())