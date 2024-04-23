texto = str(input('Digite um nome: '))
VOGAIS = 'AEIOU'

for l in texto:
    if l.upper() in VOGAIS:
        print(l, end="")
        
else:
    print()        


for c in range(0, 10):
    print(c, end='')

