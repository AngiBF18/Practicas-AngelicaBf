#juego de cartas 

import random

#la lista de cartas
cartas = []
figuras= ["diamantes", "corazones", "treboles","picas"]

# Llenar las cartas con sus número y figuras
for numero in range(1, 14):  # Del 1 al 13
    for figura in figuras:
        cartas.append(f"{numero} de {figura}")

# Barajear
random.shuffle(cartas)

# listas del mazo barajado y los puntos
MAZO_barajado = []
PUNTOS_jugador = 0
PUNTOS_computadora = 0

# Barajar las cartas y repetir
while cartas:
    carta = cartas.pop()  # Tomar una carta al azar
    MAZO_barajado.append(carta)

# Es hora de jugar 
while len(MAZO_barajado) > 1:
    CARTA_ahora = MAZO_barajado.pop()
    SIGUIENTE_carta = MAZO_barajado[-1]

    print(f"Tu carta es: {CARTA_ahora}")
    print("¿Selecciona una de estas dos opciones: 'batalla' o 'siguiente'?")
    respuesta = input().strip().lower()

    # Si la carta de ahora tiene el mismo punto
    if CARTA_ahora.split()[0] == SIGUIENTE_carta.split()[0]:
        if respuesta == "batalla":
            PUNTOS_jugador += 1
            print(f"¡Batalla! Has adquirido un punto. Tu puntaje actual es de : {PUNTOS_jugador}")
        else:
            PUNTOS_computadora += 1
            print(f"¡Batalla! La computadora te ha vendico, por ende, ella gana un punto. El puntaje de la computadora es : {PUNTOS_computadora}")
    else:
        print("No es una batalla.")

# Final 
if PUNTOS_jugador > PUNTOS_computadora:
    print(f"\n¡Felicitaciones! lo has logrado con {PUNTOS_jugador} puntos.")
elif PUNTOS_computadora > PUNTOS_jugador:
    print(f"\n¡Para la próxima! La computadora te ha ganado con {PUNTOS_computadora} puntos.")
else:
    print(f"\n¡Empate! la computadora y tú tiene  {PUNTOS_jugador} puntos.")