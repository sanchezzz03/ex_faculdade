# sequência de fibonacci

num_inicial = 0
num_atual = 1

tamanho = int(input("digite o tamanho da sequencia que deseja: "))

for i in range((tamanho)):
    proximo = num_inicial + num_atual
    num_inicial = num_atual
    num_atual = proximo

print(num_inicial)
# assim mostra apenas o número no indice que foi escolhido
# caso deixe o print no inicio do loop mostrará a sequência inteira