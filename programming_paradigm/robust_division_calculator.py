def safe_divide(numerator, denominator):
    """
    Performs division with error handling for division by zero and non-numeric inputs.
    
    Args:
    numerator (str): The dividend.
    denominator (str): The divisor.
    
    Returns:
    str: The result of the division or an error message.
    """
    
    # Attempt to convert inputs to floats
    try:
        numerator = float(numerator)
        denominator = float(denominator)
    except ValueError:
        return "Error: Please enter numeric values only."
    
    # Perform division with zero division error handling
    try:
        result = numerator / denominator
        # Remove trailing zeros
        result_str = f"{result:g}"
        return f"The result of the division is {result_str}"
    except ZeroDivisionError:
        return "Error: Cannot divide by zero."
