class Person:
    population = 0  # class variable to keep track of the population
    
    def __init__(self, name, age):
        """
        Constructor for Person class. Initializes name and age of person, and increments population.
        """
        self.name = name
        self.age = age
        Person.population += 1  # increment the population when a new person is created
    
    def display_info(self):
        """
        Displays the name and age of the person.
        """
        print(f"{self.name} is {self.age} years old.")
    
    @staticmethod
    def is_adult(age):
        """
        Returns True if the age is greater than or equal to 18, else returns False.
        """
        return age >= 18
    
    @classmethod
    def get_population(cls):
        """
        Returns the current population of the Person class.
        """
        return cls.population


person1 = Person("Alice", 25)
person2 = Person("Bob", 16)
person3 = Person("Charlie", 40)

person1.display_info()  # output: "Alice is 25 years old."
print(Person.is_adult(person1.age))  # output: True
print(Person.is_adult(person2.age))  # output: False

print(Person.get_population())  # output: 3
