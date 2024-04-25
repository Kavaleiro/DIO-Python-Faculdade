itens = []
n = 3
for i in range(n):
    item = input(f"Digite o {1+i} item: ")
    itens.append(item)
    
# Exibe a lista de itens
print("Lista de itens:")
for item in itens:
    print(f"- {item}")