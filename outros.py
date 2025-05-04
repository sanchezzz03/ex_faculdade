#def teste():
#    nums1 = [1, 3]
#    nums2 = [2, 4]
#    total = sorted(nums1 + nums2)
#    mediana=[]
#    indice = len(total)
#    if indice % 2 == 0:
#        #aqui é o termo do meio/menor (-1 por que o indice começa em 0)
#        mediana.append(total[(indice//2) - 1 ])
#        # aqui é o termo do meio/maior
#        mediana.append(total[indice//2])
#        media = 0
#        valor = 0
#        c = 0
#        for i in mediana:
#            c+=1
#            valor = valor + i
#        media = valor / c
#        mediana = media
#
#    else:
#        mediana = total[indice//2]
#    return(mediana,total)
#
#mediana, total = teste()
#print(f'{total} e a mediana é {mediana}')

#for i in range (10,20):
#    for j in range (10,20, 2):
#        print('{} + {} = {}'.format(i,j,i+j))

num=int(input("digite um numero"))
str_num=str(num)
lista=[]
for i in str_num:
    lista.append(int(i))

lista.sort()
print(lista)


#letra=input("\nDigite uma letra: ")
#alfabeto=["a","b","c","d","e","f","g","h","i",
#          "j","k","l","m","n","o","p","q","r",
#          "s","t","u","v","w","x","y","z"]
#c=0
#total_criptograf=""
#
#for carac in letra:
#   for alf in alfabeto:
#       c+=1
#       if carac==alf:
#            total_criptograf+=str(c)
#            c=0
#            break
#
#print(f"o valor da letra digitada é {total_criptograf}")