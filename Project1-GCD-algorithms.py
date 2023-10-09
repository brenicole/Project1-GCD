#Breanna Woosley
#CSC 2400-003 Design of Algorithms
#Project 1
#find gcd using Euclidean, conseutive integer check, and middle school procedure
#September 8, 2023


# Input values for m and n
# validate they are positive integers
try:
    m = int(input("Enter the first positive integer (m): "))
    n = int(input("Enter the second positive integer (n): "))
except ValueError:
    print("Both inputs must be integers.")


if m < 1 or n < 1:
    print("Both inputs must be positive integers.")



# Extended Euclidean Algorithm
def extended_euclidean_gcd(m, n):
    if n == 0:
        return (m, 1, 0)
    else:
        # Recursive call to compute GCD and coefficients
        d, x, y = extended_euclidean_gcd(n, m % n)
        return (d, y, x - (m // n) * y)

# Consecutive Integer Checking Algorithm
def gcd_consecutive_integer(m, n):
    if m<n:
        m, n=n, m # swap m and n if m is smaller
    while n>0:
        m, n=n, m % n
    return m

# Middle School Procedure
#find common factors between the two numbers and iteratively
# reducing the larger number until a common factor is found.

def gcd_middle_school_procedure(m, n):
    #Find the prime factors of 'm'
    prime_factors_m = []
    factor = 2

    while m > 1:
        while m % factor == 0:
            prime_factors_m.append(factor)
            m //= factor
        factor += 1

    #Find the prime factors of 'n'
    prime_factors_n = []
    factor = 2

    while n > 1:
        while n % factor == 0:
            prime_factors_n.append(factor)
            n //= factor
        factor += 1

    #Find the common prime factors
    common_factors = []

    for factor in prime_factors_m:
        if factor in prime_factors_n:
            common_factors.append(factor)
            prime_factors_n.remove(factor)


    # Step 4: Calculate the GCD by multiplying common prime factors
    gcd = 1

    for factor in common_factors:
        gcd *= factor

    return gcd

# Results using three methods
extended_gcd_result = extended_euclidean_gcd(m, n)
consecutive_integer_result = gcd_consecutive_integer(m, n)
middle_school_result = gcd_middle_school_procedure(m, n)

# Display the results
print(f"GCD({m}, {n}) using Extended Euclidean Algorithm = {extended_gcd_result[0] if extended_gcd_result[0] != 1 else 'undefined'}")
print(f"GCD({m}, {n}) using Consecutive Integer Checking Algorithm = {consecutive_integer_result if consecutive_integer_result != 1 else 'undefined'}")
print(f"GCD({m}, {n}) using Middle School Procedure = {middle_school_result if middle_school_result != 1 else 'undefined'}")
