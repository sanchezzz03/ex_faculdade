print("\nBem-vindo à Copiadora do Lucas Sanchez Vicente!")

# Função para escolher o tipo de serviço
def escolha_servico():
    print('-' * 40)
    print("DIG - Digitalização (R$ 1,10/página)")
    print("ICO - Impressão colorida (R$ 1,00/página)")
    print("IPB - Impressão Preto e Branco (R$ 0,40/página)")
    print("FOT - Fotocópia (R$ 0,20/página)")
    print('-' * 40)

    while True:
        servico = input("Digite o tipo de serviço desejado: ").upper()
        if servico == "DIG":
            return 1.10
        elif servico == "ICO":
            return 1.00
        elif servico == "IPB":
            return 0.40
        elif servico == "FOT":
            return 0.20
        else:
            print("ERRO: valor inválido. Tente novamente.")

# Função para digitar o número de páginas e calcular desconto
def num_pagina():
    while True:
        try:
            pag = int(input("Digite o número de páginas que deseja: "))
            if pag <= 0:
                print("Número inválido. Digite um valor positivo.\n")
            elif pag >= 20000:
                print("Não aceitamos pedidos com 20000 páginas ou mais. Tente novamente.\n")  # [SAÍDA DE CONSOLE 3]
            elif pag < 20:
                return pag, 0
            elif pag < 200:
                return pag, 15
            elif pag < 2000:
                return pag, 20
            else:
                return pag, 25
        except ValueError:
            print("Digite apenas números inteiros.\n")

# Função para escolher serviço extra
def servico_extra():
    while True:
        print('-' * 40)
        print("0 - Não adicionar nada (R$ 0)")
        print("1 - Encadernação simples (R$ 15)")
        print("2 - Encadernação capa dura (R$ 40)")
        print('-' * 40)
        try:
            extra = int(input("Escolha o serviço extra (0, 1 ou 2): "))
            if extra == 0:
                return 0
            elif extra == 1:
                return 15
            elif extra == 2:
                return 40
            else:
                print("Opção inválida. Digite 0, 1 ou 2.\n")
        except ValueError:
            print("Digite apenas números válidos.\n")

# Execução principal do programa
preco = escolha_servico()
pag, desconto = num_pagina()
valor_extra = servico_extra()

# Aplica desconto na quantidade de páginas
paginas_com_desconto = pag * (1 - desconto / 100)

# Cálculo final
subtotal = preco * paginas_com_desconto
total = subtotal + valor_extra

# Exibe resumo final do pedido
print("\nRESUMO DO PEDIDO:")
print(f"Total: R$ {total:.2f} (preço do serviço: R$ {preco:.2f} * páginas com desconto: {paginas_com_desconto:.2f} + extra: R$ {valor_extra:.2f})")
