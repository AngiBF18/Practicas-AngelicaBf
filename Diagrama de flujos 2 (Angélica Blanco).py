#Flujo grama con ciclos

def año_bisiesto(año):
    if (año % 4 == 0 and (año % 100 != 0 or año % 400 == 0)):
        return True
    return False

def bisiestos_conciclo(año):
    contador = 0
    for i in range(1900, año + 1):
        if año_bisiesto(i):
            contador += 1
    return contador

#año entre 1900 y 2199
año = int(input("Ingrese un año entre 1900 y 2199: "))
while año < 1900 or año > 2199:
    año = int(input("Se ha pasado del rango, ingrese un año entre 1900 y 2199: "))

#Calculo total
bisiestos = bisiestos_conciclo(año)
print(f"Desde 1900 hasta {año} el número de años bisiestos es de {bisiestos}")