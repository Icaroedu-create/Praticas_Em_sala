idade = int(input("digite a sua idade:"))
matricula = input("A matricula esta ativa [Sim/NÃO]?").uppercls
if idade >= 18 and matricula == "SIM":
    print("Acesso liberado!")
else:
    print("Acesso negado!")