#RECTANGLE AREA CALCULATOR
# Create Rectangle class
class Rectangle:
    
    # Initialize length and breadth
    def __init__(self, length, breadth):
        self.length = length
        self.breadth = breadth
    
    # Method to calculate area
    def calculate_area(self):
        return self.length * self.breadth
    
    # Method to update dimensions
    def update_dimensions(self, new_length, new_breadth):
        self.length = new_length
        self.breadth = new_breadth


# Create object and test methods
rect = Rectangle(10, 5)

# Calculate initial area
print("Initial Area:", rect.calculate_area())

# Update dimensions
rect.update_dimensions(20, 8)

# Calculate updated area
print("Updated Area:", rect.calculate_area())