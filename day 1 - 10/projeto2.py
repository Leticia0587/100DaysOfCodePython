print("Bem vindo a calculadora de divisão de conta!!")
conta = float(input("Qual o valor total da compra? "))
num_pessoas = input("A conta será dividida em quantas pessoas?")
gorjeta = input("Qual é a taxa da gorjeta? ")

total_conta = float(conta)
num_pessoas = int(num_pessoas)
div_conta = total_conta / num_pessoas
porcetagem_gorjeta = float(gorjeta) / 100

total_conta_por_pessoa = round(div_conta + (porcetagem_gorjeta * div_conta), 2)

print(f"O valor a ser pago por pessoa é: ${total_conta_por_pessoa}")
