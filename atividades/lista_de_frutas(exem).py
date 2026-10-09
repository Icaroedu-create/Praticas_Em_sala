frutas = ["maça","banana","uva","laranja"]
#alterando indice


          
          
          #adicionando elementos
          
#adiciona um elemento a ultima posição da lista 

frutas.append("melancia")

#adiciona elementos a uma posiçâo da lista 

frutas.insert(1,"pera")

#adicionando varios elementos a lista

frutas.extend(["kiwi","manga"])

#verificando existençia do elemento na lista 

verificar = "maça" in frutas 
print(verificar)

#Verificando a quantidade de elementos na lista 

quantidade_de_elementos = len(frutas)
print(quantidade_de_elementos)

#contando elementos 

contador = frutas.count("pera")
print(contador)

#retornando o indice do valor 

indice = frutas.index("pera")
print(f"A fruta do indice {indice}, corresponde ao elemento 
{frutas[indice]}")

#fazendo uma copia da lista

lista = frutas.copy()
lista.append("melancia")
print(listas)
contador = listas.count("Melancia")
print(contador)

#