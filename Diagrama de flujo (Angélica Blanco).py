#Flujo grama sin ciclos 

def año_bisiesto(año):
    if(año % 4 == 0 and (año % 100 != 0 or año % 400 == 0)):
        return True
    return False 

def bisiesto_sinciclo(año): 
    # Múltiplos de 4, 100 y 400
    bisiestos = año // 4 - año // 100 + año // 400
    return bisiestos

# Año entre 1900 y 2199
año = int(input("Escriba un año entre 1900 y 2199: "))
while año < 1900 or año > 2199:
    año = int(input("Se ha pasado del rango, ingrese un año entre 1900 y 2199: "))

# Cálculo del número de años bisiestos
bisiestos = bisiesto_sinciclo(año)

# Mostrar el resultado
print(f"Desde 1900 hasta {año} el número de años bisiestos es de {bisiestos}")

