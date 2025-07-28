'''
clamethod: not the instanes ,class bound
class class(1st arg)
@classmethod
class:'''
class student:
    def __init__(s, name, marks):
        s.name=name
        s.marks=marks
    def display(self):
        print(f"Student name:{s.name}")
        print(f"Student marks:{s.marks}")
name=str(input("Enter the name:"))
marks=int(input("Enter the marks:"))
s=student(name,marks)
s.display()