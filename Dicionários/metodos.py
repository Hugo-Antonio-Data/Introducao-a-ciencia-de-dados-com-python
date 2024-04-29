contatos ={
    "hugo@gmail.com":{"nome": "Hugo", "idade": 28, "telefone": "3333 - 3333"},
    "amanda@gmail.com":{"nome": "Amanda", "idade": 28, "telefone": "4444 - 4444"},
    "adja@gmail.com":{"nome:": "Adja", "idade": 25, "telefone": "5555 - 5555", "extra":{"a": 1}}

}
contatos.clear()
print(contatos)
contatos["lucrecio@gmail.com"] = {"nome": "Lucrecio", "idade": 28, "telefone": "7777-7777"}
print(contatos)
copia = contatos.copy()
copia["lucrecio@gmail.com"] = {"nome": "Lu", }
print(copia)

#contatos["chave"]
resultado = contatos.get("chave")
print(resultado)

resultado = contatos.get("chave", {})
print(resultado)
resultado = contatos.get("lucrecio@gmail.com", {})
print(resultado)

alunos = {"matricula1":{"nome": "Hugo", "idade": 28, "formacao": "ads"}}
print(alunos.items())
print(alunos.keys())
print(alunos.values())
#print(alunos.pop("idade")) exclui apenas a chave e você tem que passar ela dentro do parenteses
print(alunos.popitem())
print(alunos)
print(alunos.setdefault('formacao', 'adm'))
alunos.update({"matricula1":{"nome": "Hugo Antonio"}})
print(alunos)
alunos.update({"matricula2":{"nome": "Amanda", "idade": 28, "formacao": "ads"}})
print(alunos)
resultado1 = "matricula1" in alunos
print(resultado1)
resultado1 = "idade" in alunos["matricula2"]
print(resultado1)
del alunos["matricula2"]["idade"]
print(alunos)

