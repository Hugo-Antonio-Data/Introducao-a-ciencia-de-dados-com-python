lista = []
lista.append(1)
lista.append('Python')
lista.append([0, 'carro', 4])
print(lista)
#lista.clear()
#print(lista)

l2 = lista.copy()
l2.append(10)
print(l2)
l2.append(1)
print(l2)
print(l2.count(1))
lista2 = ['Maça', 3, 'Hugo']
lista2.extend(['moto', 3])
print(lista2)
print(lista2.index(3))
lista2.pop()
# o pop remove o ultimo elemento ou indice indicado dentro do parenteses
print(lista2)
lista2.remove(3)
# remove com o elemento indicado dentro do parenteses
print(lista2)
lista2.reverse()
# muda a ordem da lista de trás pra frente
print(lista2)
lista2.append('Brama')
lista2.sort()
# muda a ordem da lista em ordem alfabetica
print(lista2)
lista2.sort(reverse=True)
print(lista2)
print(len(lista2))