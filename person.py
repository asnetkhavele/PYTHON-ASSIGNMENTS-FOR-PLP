class Person:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender
    
    def introduce(self):
        print(f"Hi, I'm {self.name}. I'm {self.age} years old and I identify as {self.gender}.")

# Creating an instance of Person
if __name__ == "__main__":
    person1 = Person("Asnet", 24, "female")
    person1.introduce()
