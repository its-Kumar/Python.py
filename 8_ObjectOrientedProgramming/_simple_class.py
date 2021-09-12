class Course:
    def __init__(self, name, ratings):
        self.name = name
        self.ratings = ratings


c1 = Course("JAVA", [1, 2, 3, 4])
print(c1.name)
print(c1.ratings)
