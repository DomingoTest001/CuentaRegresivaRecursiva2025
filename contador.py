"""
Módulo contador.py
Contiene funciones para realizar cuenta regresiva recursiva
y determinar si los números son pares o impares.
"""

def es_par_o_impar(numero):
    """
    Función auxiliar que determina si un número es par o impar.
    
    Args:
        numero (int): El número a evaluar
        
    Returns:
        str: "par" si el número es par, "impar" si es impar
    """
    return "par" if numero % 2 == 0 else "impar"

def cuenta_regresiva(n):
    """
    Función recursiva que imprime los números desde n hasta 0,
    indicando si cada número es par o impar.
    
    Args:
        n (int): El número desde donde comenzar la cuenta regresiva
    """
    # Caso base: cuando llegamos a 0
    if n < 0:
        return
    
    # Mostrar el número actual con su paridad
    paridad = es_par_o_impar(n)
    print(f"{n} - {paridad}")
    
    # Llamada recursiva con n-1
    cuenta_regresiva(n - 1)

def cuenta_regresiva_con_mensaje(n):
    """
    Variante creativa: cuenta regresiva con mensaje especial al llegar a 0.
    
    Args:
        n (int): El número desde donde comenzar la cuenta regresiva
    """
    # Caso base: cuando llegamos a 0
    if n < 0:
        print("🚀 ¡Despegue exitoso! ¡La cuenta regresiva ha terminado!")
        return
    
    # Mostrar el número actual con su paridad
    paridad = es_par_o_impar(n)
    
    if n == 0:
        print(f"🎯 {n} - {paridad} - ¡CERO ALCANZADO!")
    else:
        print(f"⭐ {n} - {paridad}")
    
    # Llamada recursiva con n-1
    cuenta_regresiva_con_mensaje(n - 1)
