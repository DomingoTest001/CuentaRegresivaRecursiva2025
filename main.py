
"""
Archivo principal main.py
Programa que solicita un número al usuario y ejecuta la cuenta regresiva recursiva.
"""

import contador

def main():
    """
    Función principal que maneja la interacción con el usuario
    y ejecuta la cuenta regresiva.
    """
    print("🌟 ¡Bienvenido a la Cuenta Regresiva Recursiva! 🌟")
    print("=" * 50)
    
    try:
        # Solicitar número al usuario
        numero = int(input("Ingresa un número entero positivo: "))
        
        # Validar que sea positivo
        if numero < 0:
            print("⚠️  Por favor, ingresa un número positivo.")
            return
        
        print(f"\n🚀 Iniciando cuenta regresiva desde {numero}...")
        print("-" * 30)
        
        # Ejecutar cuenta regresiva básica
        contador.cuenta_regresiva(numero)
        
        print("\n" + "=" * 50)
        
        # Preguntar si quiere ver la versión con mensaje especial
        respuesta = input("\n¿Quieres ver la versión con mensaje especial? (s/n): ").lower()
        
        if respuesta in ['s', 'sí', 'si', 'y', 'yes']:
            print(f"\n🎨 Versión especial - Cuenta regresiva desde {numero}...")
            print("-" * 40)
            contador.cuenta_regresiva_con_mensaje(numero)
        
        print("\n✨ ¡Gracias por usar el programa!")
        
    except ValueError:
        print("❌ Error: Debes ingresar un número entero válido.")
    except Exception as e:
        print(f"❌ Error inesperado: {e}")

if __name__ == "__main__":
    main()
