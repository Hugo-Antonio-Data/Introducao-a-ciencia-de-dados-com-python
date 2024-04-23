"""
opcao = -1

while opcao != 0:
    opcao = int(input('[1] Sacar, \n[2] Extrato, \n[0] Sair \n: '))
    if opcao == 1:
        print('Sacando')
    elif opcao == 2:
        print('Exibido e Extrato')
    else:
        print('Sair')

else:
    print('Obrigado por utilizar nosso sistema!')    
"""

while True:
    numero = int(input('Digite um número: '))
    
    if numero == 10:
        break

    elif numero % 2 == 0:
        continue
    
    else:
        print(numero)

    