print("\nBem-vindo à Loja de Gelados do Lucas Sanchez Vicente!")

# Cabeçalho do cardápio
print('-' * 50)
print('-' *  20  + " Cardápio " + '-' * 20 )
print('-' * 50)

# Listas de sabores e tamanhos válidos
sabores = ["CP", "AC"]
tamanhos = ["P", "M", "G"]

# Preços dos produtos por sabor e tamanho
valores_CP = [9, 14, 18]
valores_AC = [11, 16, 20]

# Impressão do cardápio formatado
print(('-'*3) + "|" + " Tamanho " + "| " + "  Cupuaçu (CP)  " + " | " + " Açaí (AC) " + " |" + ('-' * 3))
for i in range(len(tamanhos)):
    print(('-'*3) + "|" + (" " * 4) + tamanhos[i] + (" " * 4) + "|" + (" " * 5) +
          f'R$ {valores_CP[i]:02}.00' + (" " * 5) + "|"+ (" " * 2) +
          f'R$ {valores_AC[i]:02}.00' + (" " * 3) + "|" + ('-' * 3))
print('-' * 50 + "\n")

# Inicialização de variáveis
total_pedido = 0
valores = []

# Loop principal do pedido
while True:

    # Input do sabor
    while True:
        sabor_user = input("Digite o sabor desejado (CP/AC): ").upper()
        if sabor_user not in sabores:
            print("Sabor inválido. Tente novamente.\n")
            continue
        break

    # Input do tamanho
    while True:
        tamanho_user = input("Digite o tamanho desejado (P/M/G): ").upper()
        if tamanho_user not in tamanhos:
            print("Tamanho inválido. Tente novamente.\n")
            continue
        break

    # Determinar índice do tamanho
    if tamanho_user == "P":
        indice_produto = 0
    elif tamanho_user == "M":
        indice_produto = 1
    else:
        indice_produto = 2

    if sabor_user == "CP":
        valores = valores_CP
        preco = valores[indice_produto]
    elif sabor_user == "AC":
        valores = valores_AC
        preco = valores[indice_produto]

    # Exibir valor do pedido
    print(f"Você pediu um {sabor_user} no tamanho {tamanho_user}: R$ {preco:.2f}\n")
    total_pedido += preco

    # Pergunta se deseja continuar
    while True:
        mais = input("Deseja pedir mais alguma coisa? (S/N): ").upper()
        if mais == "S":
            break
        elif mais == "N":
            # Encerra o programa
            print(f"\nO valor total a ser pago é: R$ {total_pedido:.2f}")
            break
        else:
            print("Opção inválida. Tente novamente.")

    if mais == "N":
        break