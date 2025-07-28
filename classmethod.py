class student:
    def __init__(self,name,marks):
        self.name=name
        self.marks=marks
    @classmethod
    def input(cls):
        name=str(input("Enter your name:"))
        marks=int(input("Enter your marks:"))
        return cls(name,marks)
    def display(self):
        print("Student name:", self.name)
        print("Student marks:", self.marks)
s=student.input()
s.display()