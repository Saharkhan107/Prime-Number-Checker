# Prime Number Checker
# Name: Sahar Iqbal
# Date: 10/19/2024

def is_prime(n):
    # Check if the number is less than 2 (not prime)
    if n <= 1:
        return False
    # Check for factors from 2 to the square root of n
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

# Example usage
print(is_prime(11))  # Output: True
print(is_prime(4))   # Output: False
print(is_prime(17))  # Output: True
print(is_prime(1))   # Output: False
print(is_prime(0))   # Output: False

