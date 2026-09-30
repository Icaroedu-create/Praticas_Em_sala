frutas = ["maça","banana","Uva","Laranja"]
frutas[0]
frutas[2]
frutas[-1]
#alterando elementos
frutas[1]= "Abacaxi"
#inserindo elementos
frutas.append("Melancia")
frutas.insert(1,"Pera")
frutas.extend(["Kiwi","Manga"])
#acessandom os elementos 
print(frutas[0])
print(frutas[2])
print(frutas[-1])
print("IMPRIMIR TODOS OS ELEMENTOS\n")
#percorrendo a lsita
for fruta in frutas:
    print(fruta)