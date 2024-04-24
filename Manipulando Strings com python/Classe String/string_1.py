nome = str(input('Digite seu nome: '))
print(nome.upper())
#deixa o que foi digitado na variavel nome maiúsculo
print(nome.lower())
#deixa o que foi digitado na variavel nome minúsculo
print(nome.title())
#deixa o que foi digitado na variavel nome com a 1 letra maiuscula e as demais minusculas
print(nome.center(10, "#"))


texto = str(input('Digite um texto: '))
print(texto.strip() + '.')
print(texto.rstrip() + '.')
print(texto.lstrip() + '.')
print(texto.center(10, "#"))
print('-'.join(texto))
