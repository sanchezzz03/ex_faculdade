print("\nBem-vindo a Loja do Lucas Sanchez Vicente!")

# loop para conferir se os valores inseridos são negativos
while True:
    try:
        valor_produto = float(input("Digite o valor unitário do produto: "))
        qtd_produto = float(input("Digite o quantidade de produtos que deseja comprar: "))
        if (valor_produto < 0) or (qtd_produto < 0):
            print("Um ou mais válores inválidos. Tente novamente. \n")
        else:
            break
    except ValueError:
        print("Erro, digite apenas números. Tente novamente.")

# calculando o valor total do pedido sem desconto
total_sem_desconto = valor_produto * qtd_produto

# conferindo o valor total e aplicando desconto se necessário
if total_sem_desconto < 2500:
    desconto = 0
elif (total_sem_desconto >= 2500) and (total_sem_desconto < 6000):
    desconto = 4
elif (total_sem_desconto >= 6000) and (total_sem_desconto < 10000):
    desconto = 7
else:
    desconto = 11

total_com_desconto = total_sem_desconto - (total_sem_desconto * (desconto/100))
print(f'O valor total SEM desconto é: R${total_sem_desconto}')

# if para caso não tenha desconto, mostrar apenas uma mensagem e não repetir o valor
if desconto == 0:
    print("Não há descontos.")
else:
    print(f'O valor total COM desconto é: R${total_com_desconto}')


