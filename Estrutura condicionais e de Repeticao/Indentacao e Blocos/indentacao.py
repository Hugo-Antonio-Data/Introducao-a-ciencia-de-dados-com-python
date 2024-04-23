#resumo sobre identação
def sacar(valor):
    saldo = 200
    if saldo >= valor:
        print('Valor sacado')
        print('Retire o dinheiro na boca do caixa')
        print(f'Seu saldo atual é: R$ {saldo - valor}')
    else:
        print(f'Saldo é menor que o valor solicitado, digite um valor abaixo de seu Saldo que é de R${saldo}')


saque_caixa = float(input('Digite o valor que deseja sacar: R$ '))
sacar(saque_caixa)