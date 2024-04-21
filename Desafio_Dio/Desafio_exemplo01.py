##
def calcular_imposto(salario):
    aliquota = 0.0
    if(salario >=0 and salario <= 1100):
        aliquota = 0.05
    elif(salario > 1100 and salario <= 2500):
        aliquota = 0.1
    elif(salario > 2500):
        aliquota = 0.15
    return aliquota * salario

valor_salario = float(input("Informe o valor do seu salario: "))
valor_beneficio = float(input("Digite o valor do benefício: "))
print(f"O seu salário é R${((calcular_imposto(valor_salario)+valor_salario)+ valor_beneficio):.2f} reais")
