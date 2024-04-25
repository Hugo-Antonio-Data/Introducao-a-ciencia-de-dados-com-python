numeros = set([1, 2, 3, 4, 5, 1])
print(numeros)
nome = set("abacaxi")
print(nome)
linguagens = {"Java", "c", 'Python', "Java"}
print(linguagens)
l = list(linguagens)
print(l[0])

for lin in linguagens:
    print(lin)


conjunto_a = {1, 2, 3}
conjunto_b = {2, 3, 4}
print(conjunto_a.union(conjunto_b))
print(conjunto_a.difference(conjunto_b))
print(conjunto_b.difference(conjunto_a))
print(conjunto_a.symmetric_difference(conjunto_b))

conjunto_c = {1, 2, 3}
conjunto_d = {4, 1, 2, 5, 6, 3}

print(conjunto_c.issubset(conjunto_d))
print(conjunto_d.issubset(conjunto_c))
print(conjunto_c.issuperset(conjunto_d))
print(conjunto_d.issuperset(conjunto_c))

conjunto_e = {1, 2, 3, 4}
conjunto_f = {5, 6, 7, 8}
conjunto_g = {1, 9}
print(conjunto_e.isdisjoint(conjunto_f))
print(conjunto_e.isdisjoint(conjunto_g))
