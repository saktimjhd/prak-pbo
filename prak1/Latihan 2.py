import math

class Shape:
    def hitungLuas(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    
    def hitungLuas(self):
        return math.pi * self.radius ** 2

radius = float(input("Masukkan jari-jari: "))

lingkaran = Circle(radius)

print("Luas lingkaran:", lingkaran.hitungLuas())
