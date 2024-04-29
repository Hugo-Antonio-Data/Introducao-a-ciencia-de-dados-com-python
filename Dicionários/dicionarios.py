pessoa = {"nome": "Hugo", "idade": 31}

print(pessoa)

pessoa2 = dict(nome = "Antonio", idade = 30)
print(pessoa2)

pessoa["telefone"] = "3333-3333"
pessoa2["telefone"] = "3333-3333"
print(pessoa)

pessoa2["nome"] = "Amanda"
pessoa2['idade'] = 36
pessoa2["telefone"] = "9999-9999"
print(pessoa2)

contatos ={
    "hugo@gmail.com":{"nome": "Hugo", "idade": 28, "telefone": "3333 - 3333"},
    "amanda@gmail.com":{"nome": "Amanda", "idade": 28, "telefone": "4444 - 4444"},
    "adja@gmail.com":{"nome:": "Adja", "idade": 25, "telefone": "5555 - 5555", "extra":{"a": 1}}

}

telefone = contatos["amanda@gmail.com"]["telefone"]
extra = contatos["adja@gmail.com"]["extra"]["a"]
print(telefone)
print(extra)

"""for k in contatos:
    print(k, contatos[k])
"""
for k, v in contatos.items():
    print(k, v)