import numpy as np

def dot_product(x: list, y: list) -> float:
    """
    Returns the dot product as a float.
    """
    result = np.dot(x, y)
    return float(result)


# Example 1
x = [1, 2, 3]
y = [4, 5, 6]

print(dot_product(x, y))  # Output: 32.0


# Example 2
x = [1, 0]
y = [0, 1]

print(dot_product(x, y))  # Output: 0.0


# Example 3
x = [-1, 2]
y = [3, -1]

print(dot_product(x, y))  # Output: -5.0