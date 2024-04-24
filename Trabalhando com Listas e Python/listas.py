lista = ['Maça', 'banana', 'goiaba']
letras = list("python")
numeros = list(range(0, 10))

pares = list()
quadrado = []

print(lista)
print(letras)
print(numeros)


print(lista[0:1])
print(letras[0:6:2])
print(numeros[::])

for n in numeros:
    if n % 2 == 0:
        pares.append(n)
    print(pares)

impares = [n for n in numeros if n % 2 == 1]
print(impares)

for indice, frutas in enumerate(lista):
    print(f'{indice}, {frutas}')

for num in numeros:
    quadrado.append(num ** 2)
    print(quadrado)

quadrado_2 = [num ** 2 for num in numeros]
print(quadrado_2)
