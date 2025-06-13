jugador_vida = 100
enemigo_vida = 50
jugador_ataque = 20
enemigo_ataque = 10
pociones = 3

print("¡Comienza el combate!")
print(f"Tus puntos de vida: {jugador_vida}")
print(f"Vida del enemigo: {enemigo_vida}")

while jugador_vida > 0 and enemigo_vida > 0:
    # Turno del jugador
    print("\n--- Tu turno ---")
    print(f"Tu vida: {jugador_vida} | Vida del Enemigo: {enemigo_vida}")
    print("1. Atacar")
    print("2. Curar")
    print("3. Rendirse")
    opcion = input("Elige una opción: ")

    if opcion == "1":
        # Ataque del jugador
        print("Atacas al enemigo.")
        enemy_damage = jugador_ataque
        enemigo_vida -= enemy_damage
        print(f"Le has quitado {enemy_damage} puntos de vida al enemigo.")
    elif opcion == "2":
        # Curar
        if pociones > 0:
            curacion = 30
            jugador_vida += curacion
            pociones -= 1
            if jugador_vida > 100:
                jugador_vida = 100
            print(f"Te has curado {curacion} puntos. Vida actual: {jugador_vida}. Pociones restantes: {pociones}")
        else:
            print("No tienes pociones.")
    elif opcion == "3":
        print("Te has rendido. Game Over.")
        break
    else:
        print("Opción no válida. Elige 1, 2 o 3.")
    
    # Verificar si el enemigo ha muerto
    if enemigo_vida <= 0:
        print("¡Has derrotado al enemigo!")
        break
    
    # Turno del enemigo
    print("\n--- Turno del Enemigo ---")
    print("El enemigo te ataca.")
    
    # Dos ataques del enemigo
    for i in range(1, 3):
        if jugador_vida <= 0:
            break
        print(f"Ataque {i}:")
        jugador_vida -= enemigo_ataque
        print(f"El enemigo te ha quitado {enemigo_ataque} puntos de vida.")
    
    # Verificar si el jugador ha muerto
    if jugador_vida <= 0:
        print("Has sido derrotado...")
        break

# Resultado final
if jugador_vida <= 0:
    print("\nGame Over. Has perdido.")
else:
    print("\n¡Victoria! Has derrotado al enemigo.")