continuar = "sim"
while continuar == "sim" or "s":
 frutas = ["maça","banana","uva","laranja"]
 novo_item = input("informe o nome da fruta para adicionar na lista: ").strip().title()
 if novo_item == "":
     print("informe o nome da fruta. Nenhum item foi adicionado. ")
 elif novo_item in frutas:
     posicao = frutas.index(novo_item)
     print(f"A {frutas[]}")
     
 else:
     frutas.append(novo_item)
     print(f"A fruta {frutas} foi adicionada com sucesso 😎")
 print(frutas)
 continuar = input("Deseja continuar [sim ou não]: ").lower
