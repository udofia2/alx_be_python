def perform_operation(num1: float, num2: float, operation: str) -> float|str:
    """
    Performs basic arithmetic operations.

    Args:
    num1 (float): The first number.
    num2 (float): The second number.
    operation (str): The arithmetic operation to perform. Accepts 'add', 'subtract', 'multiply', or 'divide'.

    Returns:
    float or str: The result of the arithmetic operation or an error message for division by zero.
    """

    # Check operation type and perform corresponding calculation
    if operation == 'add':
        return num1 + num2
    elif operation == 'subtract':
        return num1 - num2
    elif operation == 'multiply':
        return num1 * num2
    elif operation == 'divide':
        # Handle division by zero
        if num2 == 0:
            return "Error: Division by zero is not allowed."
        return num1 / num2
    else:
        # Handle invalid operation
        return "Error: Invalid operation. Please choose 'add', 'subtract', 'multiply', or 'divide'."


# Example usage (not required for main.py testing)
if __name__ == "__main__":
    print(perform_operation(5, 6, 'add'))  # Output: 11.0
    print(perform_operation(5, 6, 'subtract'))  # Output: -1.0
    print(perform_operation(5, 6, 'multiply'))  # Output: 30.0
    print(perform_operation(5, 6, 'divide'))  # Output: 0.8333333333333334
    print(perform_operation(5, 0, 'divide'))  # Output: Error: Division by zero is not allowed.
    print(perform_operation(5, 6, 'modulus'))  # Output: Error: Invalid operation. Please choose 'add', 'subtract', 'multiply', or 'divide'.
