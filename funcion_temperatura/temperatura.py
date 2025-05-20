import random

def generar_temperaturas_aleatorias(cantidad=4, min_temp=-10, max_temp=99):
    """
    Genera una lista de temperaturas aleatorias únicas.

    Args:
        cantidad (int): El número de temperaturas a generar. Por defecto es 4.
        min_temp (int): La temperatura mínima posible. Por defecto es -10.
        max_temp (int): La temperatura máxima posible. Por defecto es 99.

    Returns:
        list: Una lista de temperaturas aleatorias únicas.
              Si no se pueden generar suficientes temperaturas únicas en un rango
              razonable, se devolverá una lista con las temperaturas únicas generadas.
    """
    if cantidad > (max_temp - min_temp + 1):
        print(f"Advertencia: La cantidad solicitada ({cantidad}) es mayor que el rango de temperaturas posibles ({max_temp - min_temp + 1}).")
        print("Se generarán todas las temperaturas únicas posibles dentro del rango.")
        return random.sample(range(min_temp, max_temp + 1), max_temp - min_temp + 1)

    temperaturas = set()
    while len(temperaturas) < cantidad:
        temp = random.randint(min_temp, max_temp)
        temperaturas.add(temp)
    return list(temperaturas)

# --- Ejemplos de uso ---

print("Temperaturas aleatorias:")
temperaturas_obtenidas = generar_temperaturas_aleatorias()
for i, temp in enumerate(temperaturas_obtenidas):
    print(f"Temperatura {i+1}: {temp}°C")