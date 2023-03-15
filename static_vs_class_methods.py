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

# In this example, we have a Person class that contains three methods: __init__(), display_info(), and is_adult().

# The __init__() method is a constructor that initializes the name and age of the person, and increments the population count.

# The display_info() method simply displays the name and age of the person.

# The is_adult() method is a static method that returns True if the age is greater than or equal to 18, and False otherwise.

# In addition to these three methods, we also have a class variable population that keeps track of the number of Person objects that have been created.
# We use a class method get_population() to retrieve the current population count.

# To summarize the differences between static and class methods:

# Static methods are methods that belong to the class, but do not depend on any instance of the class.
# They are useful for operations that do not need to access any instance variables or methods.

# Class methods are methods that belong to the class and can access class-level data (such as class variables).
# They are useful for operations that need to operate on the class as a whole. To access class-level data, we use the cls parameter instead of self.


