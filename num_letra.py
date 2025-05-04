letra=input("\nDigite uma letra: ")
alfabeto=["a","b","c","d","e","f","g","h","i",
          "j","k","l","m","n","o","p","q","r",
          "s","t","u","v","w","x","y","z"]
c=0
total_criptograf=""

for carac in letra:
   for alf in alfabeto:
       c+=1
       if carac==alf:
            total_criptograf+=str(c)
            c=0
            break

print(f"o valor das letras digitadas é {total_criptograf}")