def safe_divide(numerator, denominator):
    """
    Performs division while safely handling common errors like
    ZeroDivisionError and ValueError for non-numeric input.

    Args:
        numerator (str): The string representation of the numerator.
        denominator (str): The string representation of the denominator.

    Returns:
        str: A message indicating the result of the division or the error that occurred.
    """
    try:
        # Attempt to convert inputs to floats
        num = float(numerator)
        den = float(denominator)

        # Check for division by zero
        if den == 0:
            return "Error: Division by zero is not allowed."

        # Perform the division
        result = num / den
        return f"Result: {result}"

    except ValueError:
        # Catch non-numeric input
        return "Error: Both inputs must be valid numbers."