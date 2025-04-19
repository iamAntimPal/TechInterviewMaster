class Shape:
    def area(self):
        return 0  

class Square(Shape):
    def __init__(self, length):
        if length <= 0:
            raise ValueError("Length must be a positive number.")
        self.length = length 
    
    def area(self):
        return self.length ** 2 

if __name__ == "__main__":
    shape = Shape()
    square = Square(5)

    print(f"Shape Area: {shape.area()}")
    print(f"Square Area: {square.area()}")
