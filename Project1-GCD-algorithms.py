#Breanna Woosley
#CSC 2400-003 Design of Algorithms
#Project 1 Corrections
#find gcd using Euclidean, conseutive integer check, and middle school procedure
#October 8 2023
#License: TNTech Education

# Input values for m and n
# validate they are integers
try:
    m = int(input("Enter the first integer (m): "))
    n = int(input("Enter the second integer (n): "))
except ValueError:
    print("Both inputs must be integers.")
    exit()

# Ensure m and n are non-negative for GCD calculation
m = abs(m)
n = abs(n)

# Check if both inputs are zero
if m == 0 and n == 0:
    print("GCD is undefined for both inputs being zero.")
else:
    # Extended Euclidean Algorithm
    def extended_euclidean_gcd(m, n):
        """
        Calculate the GCD of two integers using the Extended Euclidean Algorithm.

        Args:
            m (int): The first integer.
            n (int): The second integer.

        Returns:
            tuple: A tuple containing the GCD and coefficients (d, x, y).
        """
        if n == 0:
            return (m, 1, 0)
        else:
            # Recursive call to compute GCD and coefficients
            d, x, y = extended_euclidean_gcd(n, m % n)
            return (d, y, x - (m // n) * y)

    # Consecutive Integer Checking Algorithm
    def gcd_consecutive_integer(m, n):
        """
        Calculate the GCD of two integers using the Consecutive Integer Checking Algorithm.

        Args:
            m (int): The first integer.
            n (int): The second integer.

        Returns:
            int: The calculated GCD.
        """
        if m < n:
            m, n = n, m  # swap m and n if m is smaller
        while n > 0:
            m, n = n, m % n
        return m

    # Middle School Procedure
    def gcd_middle_school_procedure(m, n):
        """
        Calculate the GCD of two integers using the Middle School Procedure.

        Args:
            m (int): The first integer.
            n (int): The second integer.

        Returns:
            int: The calculated GCD.
        """
        # Find the common factors between the two numbers
        while n != 0:
            m, n = n, m % n
        return m

    # Results using three methods
    extended_gcd_result = extended_euclidean_gcd(m, n)
    consecutive_integer_result = gcd_consecutive_integer(m, n)
    middle_school_result = gcd_middle_school_procedure(m, n)

    # Display the results
    print(f"GCD({m}, {n}) using Extended Euclidean Algorithm = {extended_gcd_result[0] if extended_gcd_result[0] != 1 else 'undefined'}")
    print(f"GCD({m}, {n}) using Consecutive Integer Checking Algorithm = {consecutive_integer_result if consecutive_integer_result != 1 else 'undefined'}")
    print(f"GCD({m}, {n}) using Middle School Procedure = {middle_school_result if middle_school_result != 1 else 'undefined'}")


