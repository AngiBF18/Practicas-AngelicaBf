print ("Receta para hacer una arepa")
# Imgredientes para preparar una arepa 
harina_PAN = ("1. Harina PAN")
agua = ("2. Agua")
aceite = ("3. Aceite")
sal = ("4. Sal")

print(harina_PAN)
print(agua)
print(aceite)
print (sal)

print ("Ingrese las cantidades a utilizar")

# Cantidades deseadas
h = int(input("Tazas de Harina:"))
a= int(input("Tazas de Agua:"))
A= float (input("Cucharadas de Aceite:"))
s= float (input("Cucharadas de Sal:"))

 #Valor total 
Bowl= a+h+s
Sarten= Bowl+A
Coción= (Sarten * 10) / 100
#Volúmen total 
print("Esta es su cantidad total:", Sarten)
print ("Este es su volumen total después de la coción:", Coción)

