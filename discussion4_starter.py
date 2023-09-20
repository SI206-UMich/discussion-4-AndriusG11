class Rectangle():
    
    def __init__(self, width, height):
        self.width = width
        self.height = height


   #test
    
    def __str__(self):
        return f"A rectangle with width {self.width} and height {self.height}"



    
    def verify_input(self):
        if self.width > 0 and self.height > 0:
            return True
        return False

    

    
    def area(self):
        input = self.verify_input()
        if input == False:
            return "Invalid input"
        return self.width * self.height



    
    def perimeter(self):
        input = self.verify_input()
        if input == False:
            return "Invalid input"
        return 2 * (self.width + self.height)


def main():
    r = Rectangle(10, 10)
    print(r)
    print("Area:", r.area())
    print("Perimeter:", r.perimeter())
    print()

    r = Rectangle(0, 10)
    print(r)
    print("Area:", r.area())
    print("Perimeter:", r.perimeter())
    print()

if __name__ == "__main__":
    main()