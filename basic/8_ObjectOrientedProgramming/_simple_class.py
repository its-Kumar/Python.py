"""Introduction to classes and objects in python."""


class Course:
    """Simple class to represent a class Course"""

    def __init__(self, name: str, ratings: "list"):
        # Validate data types
        assert isinstance(name, str), "name should be a str"
        assert isinstance(ratings, list), "ratings should be a list"
        assert name != "", "name should not be empty."

        # instantiate the object
        self.name = name
        self.ratings = ratings

    def __repr__(self):
        return f"{self.__class__.__name__}({self.name}, {self.ratings})"


c1 = Course("JAVA", [1, 2, 3, 4])
print(c1.name)
print(c1.ratings)

c2 = Course("PYTHON", [1, 2, 3, 4, 5])
print(c2.name)
print(c2.ratings)

print(c1)
print(c2)
print(c1.__dict__)
