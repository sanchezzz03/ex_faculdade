def teste():
    # caso queira digitar a lista de numeros
    # tamanho = int(input("digite o tamanho da lista que deseja criar: "))
    # total = []
    # for i in range (tamanho):
    #   carac = int(input("digite o número que deseja adicionar: "))
    #   total.append(carac)
    #   total.sorted()
    nums1 = [1, 3]
    nums2 = [2]
    total = sorted(nums1 + nums2)
    mediana=[]
    indice = len(total)
    if indice % 2 == 0:
        #aqui é o termo do meio/menor (-1 por que o indice começa em 0)
        mediana.append(total[(indice//2) - 1 ])
        # aqui é o termo do meio/maior
        mediana.append(total[indice//2])
        media = 0
        valor = 0
        c = 0
        for i in mediana:
            c+=1
            valor = valor + i
        media = valor / c
        mediana = media
    else:
        mediana = total[indice//2]
    return(mediana,total)

mediana, total = teste()
print(f'{total} e a mediana é {mediana}')