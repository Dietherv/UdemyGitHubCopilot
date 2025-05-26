def sumar(a, b):
    """
    Suma dos números (pueden ser enteros o flotantes) y devuelve el resultado.

    Args:
        a (int | float): Primer número.
        b (int | float): Segundo número.

    Returns:
        int | float: La suma de a y b.
    """
    return a + b

def es_par(numero: int) -> bool:
    """
    Determina si un número es par.

    Args:
        numero (int): Número a evaluar.

    Returns:
        bool: True si el número es par, False si es impar.
    """
    return numero % 2 == 0

