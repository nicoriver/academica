# Calculadora de Gastos Personales
# Permite ingresar múltiples gastos y calcular el total

print("=== CALCULADORA DE GASTOS ===")
print("Ingresa tus gastos y calcula el total")
print("-" * 35)

# Variables para almacenar los datos
total_gastos = 0
cantidad_gastos = 0
lista_gastos = []

# Bucle principal para ingresar gastos
while True:
    print(f"\n--- Gasto #{cantidad_gastos + 1} ---")
    
    # Entrada de datos - descripción del gasto
    descripcion = input("Descripción del gasto (o 'salir' para terminar): ")
    
    # Estructura condicional para salir
    if descripcion.lower() == 'salir':
        break
    
    # Entrada de datos - monto del gasto
    try:
        monto = float(input("Monto del gasto: $"))
        
        # Validación con estructura condicional
        if monto < 0:
            print("  El monto no puede ser negativo. Intenta nuevamente.")
            continue
        elif monto == 0:
            print(" El monto no puede ser cero. Intenta nuevamente.")
            continue
        else:
            # Operaciones matemáticas
            total_gastos += monto
            cantidad_gastos += 1
            
            # Almacenar el gasto en la lista
            lista_gastos.append({"descripcion": descripcion, "monto": monto})
            
            print(f" Gasto agregado: {descripcion} - ${monto:.2f}")
            
    except ValueError:
        print("  Por favor ingresa un número válido.")
        continue

# Mostrar resultados finales
print("\n" + "=" * 40)
print("RESUMEN DE GASTOS")
print("=" * 40)

if cantidad_gastos > 0:
    # Mostrar cada gasto registrado
    print(f"\nGastos registrados ({cantidad_gastos}):")
    for i, gasto in enumerate(lista_gastos, 1):
        print(f"{i}. {gasto['descripcion']}: ${gasto['monto']:.2f}")
    
    # Cálculos adicionales
    promedio_gastos = total_gastos / cantidad_gastos
    
    print(f"\n--- TOTALES ---")
    print(f"Total de gastos: ${total_gastos:.2f}")
    print(f"Cantidad de gastos: {cantidad_gastos}")
    print(f"Promedio por gasto: ${promedio_gastos:.2f}")
    
    # Análisis con estructuras condicionales
    print(f"\n--- ANÁLISIS ---")
    if total_gastos > 150000:
        print("Has gastado más de $1000. Considera revisar tu presupuesto.")
    elif total_gastos > 100000:
        print("Gastos moderados. Mantén el control de tu presupuesto.")
    else:
        print("Gastos controlados. ¡Buen manejo del dinero!")
    
    # Encontrar el gasto más alto y más bajo
    gasto_mayor = max(lista_gastos, key=lambda x: x['monto'])
    gasto_menor = min(lista_gastos, key=lambda x: x['monto'])
    
    print(f"\nGasto más alto: {gasto_mayor['descripcion']} (${gasto_mayor['monto']:.2f})")
    print(f"Gasto más bajo: {gasto_menor['descripcion']} (${gasto_menor['monto']:.2f})")
    
else:
    print("No se registraron gastos.")

print("\n¡Gracias por usar la aplicacion!")
