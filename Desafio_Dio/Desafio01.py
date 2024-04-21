quantidade_passos = int(input("Quantidade de passos: "))

if quantidade_passos < 0:
    print("Não existe passos Negativos")
elif quantidade_passos == 0:
    print("Nenhum passo foi dado.")
else:
    for n in range(quantidade_passos):
        print(f"Passo {n+1}")
