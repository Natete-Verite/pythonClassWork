class Circle:
    def __init__(self,r):
        self.r = r 
    def area(self):
        A = 3.14*(self.r)*(self.r)
        return f"The area is {A}"
    def circumference(self):
        C = 2*3.14*(self.r)
        return f"The circumference is {C}"  

class Square:
    def __init__(self,a):
        self.a = a
    def area(self):
        A = (self.a)*(self.a)
        return f"The area is {A}"   
    def perimeter(self):
        P = 4*(self.a)
        return f"The perimeter is {P}"  

class Rectangle:
    def __init__(self,w,l):
        self.w = w
        self.l = l
    def area(self):
        A = self.w * self.l 
        return f"The area is {A}"
    def perimeter(self):
        P = 2*(self.w + self.l)
        return f"The perimeter is {P}" 

class Sphere:
    def __init__(self,r):
        self.r = r
    def area(self):
        A = (4*3.14)*(self.r)*(self.r)
        return f"The area is {A}"    
    def perimeter(self):
        P = (4/3)*3.14*(self.r**3)
        return f"The perimeter is {P}" 