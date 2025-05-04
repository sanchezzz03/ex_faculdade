num=int(input("digite um numero"))
str_num=str(num)
lista=[]
for i in str_num:
    lista.append(int(i))

lista.sort()
print(lista)