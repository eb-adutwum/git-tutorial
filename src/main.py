def div(x, y):
    """Divide two numbers."""
    if y == 0:
        raise ZeroDivisionError("Cannot divide by zero.")
    return x / y