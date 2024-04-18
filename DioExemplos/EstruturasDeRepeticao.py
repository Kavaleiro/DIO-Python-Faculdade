#Comando FOR
texto = "tEXTO"
VOGAIS = "AEIOU"

for letra in texto:
    if letra.upper() in VOGAIS:
        print(letra, end="")
else:    
    print()

#RANGE
for numero in range(0, 11):
    print(numero, end="")

#WHILE
cont = 1
while cont !=0:
    cont = int(input("Digite um numero: [0]sair"))
    print(f"Você digitou o numero {cont}!!")
