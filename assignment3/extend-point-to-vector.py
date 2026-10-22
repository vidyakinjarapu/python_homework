import math
class Point():
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def equality(self, other):
        return self.x == other.x and self.y == other.y
    def string_representation(self):
        return f"coordinates of Point are {self.x}, {self.y}"
    def Euclidian_distance(self, other):
        return math.sqrt((self.x - other.x)**2 + (self.y - other.y)**2)

class Vector(Point):
    def __init__(self, x, y):
        super().__init__(x, y)
    
    def __add__(self, other):
         new_x = self.x + other.x
         new_y = self.y + other.y
         return Vector(new_x, new_y)
    
    def __str__(self):
            return f"coordinates of vector are {self.x}, {self.y}"


p1 = Point(2, 3)
p2 = Point(4, 5)
v1 = Vector(3, 4)
v2 = Vector(5, 6)


print(p1.equality(p2))
print(p1.string_representation())
distance = p1.Euclidian_distance(p2)
print("Euclidian distance is : ", distance)

v3 = v1 + v2
print(v3.str())
