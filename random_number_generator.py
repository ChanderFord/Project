import random


def generate_random_number(min_value=1, max_value=100):
    """Generate a random integer between min_value and max_value (inclusive)."""
    return random.randint(min_value, max_value)


def generate_random_float(min_value=0.0, max_value=1.0):
    """Generate a random float between min_value and max_value."""
    return random.uniform(min_value, max_value)


def generate_random_numbers(count, min_value=1, max_value=100):
    """Generate a list of random integers."""
    return [random.randint(min_value, max_value) for _ in range(count)]


if __name__ == "__main__":
    print("Random Number Generator")
    print("-" * 30)

    num = generate_random_number()
    print(f"Random integer (1-100): {num}")

    float_num = generate_random_float()
    print(f"Random float (0.0-1.0): {float_num:.4f}")

    nums = generate_random_numbers(5)
    print(f"5 random integers (1-100): {nums}")

    custom = generate_random_number(min_value=50, max_value=200)
    print(f"Random integer (50-200): {custom}")
