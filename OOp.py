class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    @staticmethod
    def college():
        print("ABC college")

    def average(self):
        sum = 0
        for a in self.marks:
            sum = sum+a
        print("Name=", self.name)
        print("Average=", sum/3)


s1 = Student("Ram", [50, 50, 50])
s1.average()
s1.college()
