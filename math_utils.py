def factorial(n):
    """
    محاسبه فاکتوریل یک عدد صحیح غیرمنفی.
    
    Args:
        n (int): عدد صحیح غیرمنفی
        
    Returns:
        int: فاکتوریل عدد n
        
    Raises:
        ValueError: اگر n منفی باشد
        TypeError: اگر n عدد صحیح نباشد
    """
    if not isinstance(n, int):
        raise TypeError("ورودی باید عدد صحیح باشد")
    if n < 0:
        raise ValueError("فاکتوریل برای اعداد منفی تعریف نشده است")
    if n == 0 or n == 1:
        return 1
    
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result