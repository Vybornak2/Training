"""Debugging Example Script.

This script contains a function `calculate_average` with intentional bugs
for debugging practice:

- Bug 1: Potential TypeError
- Bug 2: Potential ZeroDivisionError
"""


def calculate_average(numbers):
    """Calculate the average of a list of numbers."""
    total: float = 0.0
    for num in numbers:
        total += num
    average = total / len(numbers)
    return average


def main():
    print("Debugging Example Script")

    data1 = [1, 2, 3, 4, 5]
    avg1 = calculate_average(data1)
    print(f"Data1: {data1}, Average: {avg1}")  # Expected: 3.0

    # Uncomment the following lines to trigger TypeError
    # data2 = [10, 20, "30", 40]
    # print(f"\nProcessing Data2: {data2}")
    # avg2 = calculate_average(data2)
    # print(f"Data2: {data2}, Average: {avg2}")

    # Uncomment the following lines to trigger ZeroDivisionError
    # data3 = []
    # print(f"\nProcessing Data3: {data3}")
    # avg3 = calculate_average(data3)
    # print(f"Data3: {data3}, Average: {avg3}")


if __name__ == "__main__":
    main()
