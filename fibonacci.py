# sequência de fibonacci

num_inicial = 0
num_atual = 1

tamanho = int(input("digite o tamanho da sequencia que deseja: "))

for i in range((tamanho-1)):
    proximo = num_inicial + num_atual
    num_inicial = num_atual
    num_atual = proximo

print(num_inicial)