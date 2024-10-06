

# Fibonacci Sequence Generator
# Asks the user for a number and
# generates a Fibonacci sequence
# of that length.

def fib_sequence(size):
    """
    Generates a Fibonacci sequence of the specified length.

    Parameters:
    size (int): The number of elements in the Fibonacci sequence.

    Returns:
    str: The Fibonacci sequence as a string of numbers separated by commas.
    """
    assert size > 0, "The size must be a positive integer."

    series = [1]  # Start the sequence with the first number

    while len(series) < size:
        if len(series) == 1:
            series.append(1)  # Add the second number (1)
        else:
            series.append(series[-1] + series[-2])  # Sum of the last two numbers

    return ', '.join(map(str, series))  # Convert the series to a string of numbers


def main():
    """
    Wrapper function that takes user input and prints the Fibonacci sequence.
    """
    try:
        user_input = int(input("How many Fibonacci numbers do you want to generate? "))
        if user_input <= 0:
            raise ValueError("Please enter a positive integer.")
        print(f"Fibonacci sequence with {user_input} numbers: {fib_sequence(user_input)}")
    except ValueError as e:
        print(f"Invalid input: {e}")


if __name__ == '__main__':
    main()
