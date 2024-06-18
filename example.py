def gcd(a, b):
    """Compute the greatest common divisor (GCD) of a and b."""
    while b:
        a, b = b, a % b
    return a

def lcm(a, b):
    """Compute the least common multiple (LCM) of a and b."""
    return abs(a * b) // gcd(a, b)

# Input from the user
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

# Calculate and print the LCM
result = lcm(num1, num2)
print(f"The LCM of {num1} and {num2} is {result}.")
