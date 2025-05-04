valor=int(input("digite a altura da piramide: "))

c=1
for i in range(valor):
   print(' ' * (valor - i) + '*' * c + ' '* (valor - i))
   c+=2