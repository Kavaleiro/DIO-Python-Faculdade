#LISTAS
frutas = ["laranja", "orange"]
letras = list("FELIPE")
#Fatiamento
print(frutas[::])
##for f in frutas:
##     print(f)
#Compreesão de Listas
numeros = [1,30,21,2,9]
pares = []
for n in numeros:
    if n % 2==0:
        pares.append(n)
