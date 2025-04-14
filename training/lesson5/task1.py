# import of Shape class from shape.py
from training.lesson5.shape import Shape

"""
## Exercise 1: Inheritance
In this exercise, you'll practice inheritance by
implementing a Rectangle and a Square class.
"""

# Here implement the Rectangle class


class Rectangle(Shape):
    pass
    # implement __init__ method with width and height
    # implement get_area method
    # implement get_perimeter method
    # implement __str__ method


# Here implement the Square class
# It should inherit from Rectangle
# Implement __init__ method with one side length


if __name__ == "__main__":
    # Test your implementation
    # Uncomment the following code when you're ready to test

    # rect = Rectangle(5, 10)
    # print(rect)  # Should display rectangle dimensions
    # print(f"Area: {rect.get_area()}")
    # print(f"Perimeter: {rect.get_perimeter()}")

    # square = Square(7)
    # print(square)  # Should display square info
    # print(f"Area: {square.get_area()}")
    # print(f"Perimeter: {square.get_perimeter()}")

    print("All tests passed!")
