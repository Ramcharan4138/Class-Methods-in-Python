'''Basic math operation using @classmethod'''
class Calculator:
    def __init__(s,a,b):
        s.a = a
        s.b = b
    @classmethod
    def input(cls):
        a=int(input("Enter the value as a:"))
        b=int(input("Enter the value as b:"))
        return cls(a,b)
    def add(s):
        return s.a+s.b
    def sub(s):
        return s.a-s.b
    def mul(s):
        return s.a*s.b
    def div(s):
        return s.a/s.b
    def floordiv(s):
        return s.a//s.b
    def mod(s):
        return s.a%s.b
    def pow(s):
        return s.a**s.b
c=Calculator.input()
print("Addition result:",c.add())
print("Subtraction result:",c.sub())
print("Multiplication result:",c.mul())
print("Division result:",c.div())
print("Floordiv result:",c.floordiv())
print("Modulus result:",c.mod())
print("Power result:",c.pow())