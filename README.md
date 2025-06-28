# 🌟 Cuenta Regresiva Recursiva 2025

## 📝 Descripción del Proyecto

Este proyecto implementa una cuenta regresiva recursiva en Python que muestra los números desde un valor dado hasta 0, indicando si cada número es par o impar. Es una actividad educativa diseñada para explorar conceptos de recursividad y modularización.

## 🎯 Objetivos Cumplidos

- ✅ Implementación de función recursiva para cuenta regresiva
- ✅ Organización del código en módulos reutilizables
- ✅ Documentación clara y completa
- ✅ Buenas prácticas de programación
- ✅ Variante creativa implementada

## 📂 Estructura del Proyecto

```
CuentaRegresivaRecursiva2025/
├── contador.py          # Módulo con funciones recursivas
├── main.py             # Archivo principal
└── README.md           # Este archivo
```

## 🚀 Cómo Ejecutar

1. Clona el repositorio:
   ```bash
   git clone https://github.com/tu-usuario/CuentaRegresivaRecursiva2025.git
   cd CuentaRegresivaRecursiva2025
   ```

2. Ejecuta el programa principal:
   ```bash
   python main.py
   ```

3. Ingresa un número entero positivo cuando se te solicite.

## 🧠 Cómo Pensé la Solución

### Análisis del Problema
La consigna requería crear una función recursiva que contara hacia atrás desde un número dado hasta 0, mostrando si cada número es par o impar. Dividí el problema en estas partes:

1. **Función auxiliar**: `es_par_o_impar()` para determinar la paridad
2. **Función recursiva principal**: `cuenta_regresiva()` para la lógica recursiva
3. **Interfaz de usuario**: En `main.py` para la interacción

### Estructura Recursiva
```python
def cuenta_regresiva(n):
    if n < 0:          # Caso base
        return
    print(f"{n} - {es_par_o_impar(n)}")  # Procesar actual
    cuenta_regresiva(n - 1)              # Llamada recursiva
```

### Decisiones de Diseño

- **Modularización**: Separé la lógica en `contador.py` y la interfaz en `main.py`
- **Reutilización**: La función `es_par_o_impar()` puede usarse en otras partes
- **Documentación**: Cada función tiene docstrings explicativos
- **Manejo de errores**: Validación de entrada y manejo de excepciones

## ✨ Variantes Creativas Implementadas

### 1. Versión con Mensaje Especial
Creé `cuenta_regresiva_con_mensaje()` que incluye:
- Emojis para hacer la salida más atractiva
- Mensaje especial al llegar a 0
- Mensaje final de "despegue exitoso"

### 2. Interfaz Mejorada
- Menú interactivo que permite elegir entre versión básica y especial
- Formato visual mejorado con separadores
- Mensajes de error descriptivos

### 3. Validaciones Adicionales
- Verificación de números positivos
- Manejo de errores de entrada
- Confirmación para ejecutar variante especial

## 🔧 Características Técnicas

- **Recursividad**: Implementación limpia sin bucles
- **Modularidad**: Código organizado en módulos separados
- **Documentación**: Docstrings en formato estándar
- **Buenas prácticas**: PEP 8, nombres descriptivos, estructura clara

## 💡 Posibles Extensiones

- Agregar cuenta progresiva (de 0 hacia arriba)
- Implementar cuenta con saltos (de 2 en 2, de 3 en 3)
- Añadir opciones de formato de salida
- Crear versión con interfaz gráfica

## 🎓 Conceptos Aprendidos

- Recursividad en Python
- Modularización de código
- Documentación de funciones
- Manejo de entrada del usuario
- Validación y manejo de errores

---

**Tiempo de desarrollo**: ~25 minutos  
**Autor**: [Tu nombre]  
**Fecha**: Junio 2025
