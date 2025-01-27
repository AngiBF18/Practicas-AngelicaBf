#Angélica Blanco

# Ciclos (loop) es lo que permite   que se repita algo mientras que se cumpla una condicion especifica.
# While == Se utiliza cuando la "condicion de parada" es clara y no se requiere un interador explicito.
# For == Se utiliza cuando la "condicion de parada" no es explicita, pero los elementos donde se va a iterar lo son.
#Batalla Pokemon
print("Soy el Profesor Oak")
while True:
    genero = input("¿Eres un chico o una chica? ").lower()
    if genero in ["chico", "chica"]:
        break
    else:
        print("Por favor, ingresa una opción válida: chico o chica.")

edad = int(input("¿Qué edad tienes? "))  # Convertir edad a entero para la comparación

if genero == "chico" and edad >= 10:
    print("¡Bienvenido al mundo Pokémon!")
elif genero == "chica" and edad >= 10:
    print("¡Bienvenida al mundo Pokémon!")
else:
    print("No tienes edad para entrenar Pokémon.")
    exit()  # Se termina el programa si no tiene la edad determinada

region = input("Necesitas un compañero de viaje, ¿en qué región te encuentras?: ").lower()

# Asignación del compañero basado en la región y el género
compañeros = {
    "kanto": {"chico": "Misty", "chica": "Brock"},
    "johto": {"chico": "Cris", "chica": "Eco"},
    "hoenn": {"chico": "Aura", "chica": "Bruno"},
    "sinnoh": {"chico": "Hoja", "chica": "Rojo"},
    "teselia": {"chico": "Maya", "chica": "León"},
    "kalos": {"chico": "Lira", "chica": "Eco"},
    "alola": {"chico": "Nanci", "chica": "Rizzo"},
    "galar": {"chico": "Gloria", "chica": "Victor"},
    "paldea": {"chico": "Juliana", "chica": "Florian"},
}

if region in compañeros and genero in compañeros[region]:
    print(f"Tu compañero de viaje es: {compañeros[region][genero]}")
else:
    print("Región o género inválido. Inténtalo de nuevo.")

# Selección de Pokémon inicial
tipo_de_pokemon = input("¿Qué tipo de Pokémon deseas? Elige entre agua, fuego y planta: ").lower()

# Diccionario de Pokémon iniciales por región y tipo
pokemon_iniciales = {
    "kanto": {"agua": "Squirtle", "fuego": "Charmander", "planta": "Bulbasaur"},
    "johto": {"agua": "Totodile", "fuego": "Cyndaquil", "planta": "Chikorita"},
    "hoenn": {"agua": "Mudkip", "fuego": "Torchic", "planta": "Treecko"},
    "sinnoh": {"agua": "Piplup", "fuego": "Chimchar", "planta": "Turtwig"},
    "teselia": {"agua": "Oshawott", "fuego": "Tepig", "planta": "Snivy"},
    "kalos": {"agua": "Froakie", "fuego": "Fennekin", "planta": "Chespin"},
    "alola": {"agua": "Popplio", "fuego": "Litten", "planta": "Rowlet"},
    "galar": {"agua": "Sobble", "fuego": "Scorbunny", "planta": "Grookey"},
    "paldea": {"agua": "Quaxly", "fuego": "Fuecoco", "planta": "Sprigatito"},
}

if region in pokemon_iniciales and tipo_de_pokemon in pokemon_iniciales[region]:
    pokemon = pokemon_iniciales[region][tipo_de_pokemon]
    print(f"Tu Pokémon inicial es: {pokemon}")
else:
    print("Tipo de Pokémon inválido. Inténtalo de nuevo.")

# Batalla simple con ataques
import random

PS_Jugador = 100
PS_Oponente = 100
defensa_oponente = 100
defensa_jugador = 100

while PS_Jugador > 0 and PS_Oponente > 0:
    ataque_jugador = input("Introduce un ataque (malicioso, placaje o ascuas): ").lower()
    
    if ataque_jugador == "malicioso":
        defensa_oponente -= 10
        print("La defensa del oponente ha bajado.")
    elif ataque_jugador == "placaje":
        daño = 35 * 100 / defensa_oponente
        PS_Oponente -= daño
        print(f"Hiciste {daño:.2f} de daño. PS del oponente: {PS_Oponente:.2f}")
    elif ataque_jugador == "ascuas":
        PS_Oponente -= 20
        print(f"Hiciste 20 de daño. PS del oponente: {PS_Oponente:.2f}")
    else:
        print("Ataque inválido. Usa malicioso, placaje o ascuas.")

    # Turno del oponente
    ataque_oponente = random.choice(["latigo", "placaje"])
    if ataque_oponente == "latigo":
        defensa_jugador -= 10
        print("El oponente usó Látigo. Tu defensa ha bajado.")
    elif ataque_oponente == "placaje":
        daño = 35 * 100 / defensa_jugador
        PS_Jugador -= daño
        print(f"El oponente usó Placaje. Recibiste {daño:.2f} de daño. Tus PS: {PS_Jugador:.2f}")

if PS_Jugador <= 0:
    print("Has perdido la batalla.")
elif PS_Oponente <= 0:
    print("¡Has ganado la batalla!")