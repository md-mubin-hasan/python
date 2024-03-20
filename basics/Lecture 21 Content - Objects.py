class SimpleSquare:
    def __init__(self, length):
        self.length = length
        
    def ares(self):
        return self.length * self.length
    
    def perimeter(self):
        return 4 * self.length

s = SimpleSquare(5)

print(s.length)
print(s.ares())
print(s.perimeter())

s.length = 10
print(s.length)
print(s.ares())
print(s.perimeter())
