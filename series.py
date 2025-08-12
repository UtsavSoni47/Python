import math

def print_series(n):
    # 1. Squares
    print("1. Squares:")
    for i in range(1, n + 1):
        print(f"{i}^2 = {i ** 2}")

    print("\n2. Sum of first n odd numbers:")
    odd_sum = 0
    current_odd = 1
    for i in range(n):
        odd_sum += current_odd
        print(f"Step {i + 1}: {odd_sum}")
        current_odd += 2

    print("\n3. Sum of first n even numbers:")
    even_sum = 0
    current_even = 2
    for i in range(n):
        even_sum += current_even
        print(f"Step {i + 1}: {even_sum}")
        current_even += 2

    print("\n4. Sum of factorials:")
    factorial_sum = 0
    for i in range(1, n + 1):
        fact = math.factorial(i)
        factorial_sum += fact
        print(f"{i}! = {fact}, Running Sum = {factorial_sum}")

    print("\n5. Sum of fractions (starting with two 1/2s):")
    frac_sum = 0
    terms = [1 / 2, 1 / 2] + [1 / i for i in range(3, n + 3)]  # Adjust range as needed
    for i, term in enumerate(terms):
        frac_sum += term
        print(f"Step {i + 1}: 1/{i + 2 if i >= 2 else 2} = {term:.4f}, Running Sum = {frac_sum:.4f}")


# Run the function with desired number of terms
n = 5
print_series(n)