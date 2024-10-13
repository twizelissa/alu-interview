#!/usr/bin/python3
def pascal_triangle(n):
    """
    Generate and print Pascal's triangle in a right triangle format up to the nth row.

    Args:
        n (int): The number of rows of Pascal's triangle to generate.

    Returns:
        list: A list of lists where each inner list represents a row 
              in Pascal's triangle. Each row contains integers.

    Description:
        - Pascal's triangle is a triangular array of binomial coefficients.
        - Each element is the sum of the two elements directly above it.
        - The first row is [1], the second row is [1, 1], and so on.

    Example:
        pascal_triangle(5) will return:
        [
            [1],
            [1, 1],
            [1, 2, 1],
            [1, 3, 3, 1],
            [1, 4, 6, 4, 1]
        ]
    
    Edge case:
        - If n <= 0, the function will return an empty list.

    """
    # If n is less than or equal to 0, return an empty list
    if n <= 0:
        return []

    # Initialize the triangle list with the first row
    triangle = [[1]]

    # Build each row from the second row (index 1) to the nth row
    for i in range(1, n):
        # Start the row with a 1
        row = [1]
        # Fill in the middle values by summing the two values above
        for j in range(1, i):
            row.append(triangle[i - 1][j - 1] + triangle[i - 1][j])
        # End the row with a 1
        row.append(1)
        # Add the completed row to the triangle
        triangle.append(row)

    # Print the triangle in a right-angled manner
    for i in range(n):
        print(" ".join(map(str, triangle[i])))  # Print each row with a space between numbers

    return triangle

# Execute the function with an example
output = pascal_triangle(5)

