idade = 20
autorizado = False
if idade >= 18 and not autorizado:
    mensagem = "arguardando autorização"
elif idade >= 18:
    mensagem = "entrada permitida"
else:
    mensagem = "entrada proibida"
print(mensagem)
