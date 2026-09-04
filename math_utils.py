def factorial(n: int) -> int:
    """
    Calculate the factorial of a non-negative integer.
    
    Args:
        n: A non-negative integer
        
    Returns:
        The factorial of n (n!)
        
    Raises:
        TypeError: If n is not an integer
        ValueError: If n is negative
    """
    if not isinstance(n, int):
        raise TypeError(f"Expected integer, got {type(n).__name__}")
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers")
    
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result