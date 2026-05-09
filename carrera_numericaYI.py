# importamos nuestro packages los cuales vamos a usar

import random randint

# Función para lanzar dados random y retornar la suma y si son pares
def lanzar_dados():
    d1 = random.randint(1, 6)
    d2 = random.randint(1, 6)
    return d1, d2, d1 + d2

def jugar():
    print("--- CARRERA NUMÉRICA ---")
    
    # 1. Entradas básicas como la de seleccionar jugadores
    n_jugadores = int(input("¿Cuántos jugadores? (2-4): "))
    print("1. Básico(20) 2. Intermedio(30) 3. Avanzado(50) 4. Experto(100)")
    opcion = int(input("Elija nivel (1-4): "))
    
    # Definir meta según la opción
    if opcion == 1: meta = 20
    elif opcion == 2: meta = 30
    elif opcion == 3: meta = 50
    else: meta = 100

    # 2. Variables de control
    posiciones = [0] * n_jugadores
    consecutivos = [0] * n_jugadores
    hay_ganador = False

    # 3. Ciclo principal del juego
    while not hay_ganador:
        for i in range(n_jugadores):
            print(f"\nTurno Jugador {i+1}")
            input("Presiona Enter para lanzar...")
            
            d1, d2, suma = lanzar_dados()
            print(f"Dados: {d1} y {d2} (Suma: {suma})")

            # Regla de los 3 pares consecutivos
            if d1 == d2:
                consecutivos[i] += 1
                print(f"¡Llevas {consecutivos[i]} pares!")
            else:
                consecutivos[i] = 0

            if consecutivos[i] == 3:
                print(f"¡EL JUGADOR {i+1} GANÓ POR TRIPLE PAR!")
                hay_ganador = True
                break

            # Movimiento normal
            posiciones[i] += suma
            print(f"Vas en la posición: {posiciones[i]}")

            if posiciones[i] >= meta:
                print(f"¡EL JUGADOR {i+1} GANÓ POR LLEGAR A LA META!")
                hay_ganador = True
                break

jugar() 