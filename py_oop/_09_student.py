class Student:
    def __init__(self, name):
        self.name = name
        self.marks = []
        print("Welcome {} to the school".format(name))
    def addmarks(self, mark):
        self.marks.append(mark)
    def avg(self):
        return sum(self.marks) / len(self.marks)


