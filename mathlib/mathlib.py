def square(n):
    """Retorna el cuadrado de un número. Soporta int/float; TypeError si no es numérico."""
    if not isinstance(n, (int, float)):
        raise TypeError("square: n debe ser un número (int o float)")
    return n * n

def factorial(n):
    """Retorna el factorial de un número para enteros positivos. TypeError si n no es int; ValueError si n < 0."""
    """Función sin errores."""
    if not isinstance(n, int):
        raise TypeError("factorial: n debe ser un entero")
    if n < 0:
        raise ValueError("factorial: n debe ser >= 0")
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result

def is_prime(n):
    """Retorna True si un número es primo, False si no. TypeError si n no es int."""
    if not isinstance(n, int):
        raise TypeError("is_prime: n debe ser un entero")
    if n < 2:
        return False
    if n % 2 == 0:
        return n == 2
    i = 3
    while i * i <= n:
        if n % i == 0:
            return False
        i += 2
    return True

def gcd(a, b):
    """Máximo común divisor. TypeError si no son enteros. ValueError si ambos son 0 (indefinido)."""
    if not isinstance(a, int) or not isinstance(b, int):
        raise TypeError("gcd: a y b deben ser enteros")
    a, b = abs(a), abs(b)
    if a == 0 and b == 0:
        raise ValueError("gcd: indefinido para 0 y 0")
    while b:
        a, b = b, a % b
    return a

def lcm(a, b):
    """Mínimo común múltiplo. TypeError si no son enteros. ValueError si ambos son 0 (indefinido)."""
    if not isinstance(a, int) or not isinstance(b, int):
        raise TypeError("lcm: a y b deben ser enteros")
    a_abs, b_abs = abs(a), abs(b)
    if a_abs == 0 and b_abs == 0:
        raise ValueError("lcm: indefinido para 0 y 0")
    return abs(a * b) // gcd(a, b)
