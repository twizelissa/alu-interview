def build_pascal_triangle(n):
    # Initialize the triangle list
    triangle = []
    
    # Build each row of the triangle
    for i in range(n):
        row = [1] * (i + 1)  # Start with a list of ones
        for j in range(1, i):  # Fill in the middle values
            row[j] = triangle[i - 1][j - 1] + triangle[i - 1][j]
        triangle.append(row)  # Add the row to the triangle

    # Print the right-aligned Pascal's Triangle
    for i in range(n):
        print(' ' * (n - i - 1), end='')  # Add leading spaces for right-alignment
        print(' '.join(map(str, triangle[i])))

# Example usage
n = 6  # Number of rows
build_pascal_triangle(n)
