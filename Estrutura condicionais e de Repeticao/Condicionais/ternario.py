saldo = float((input('Digite seu saldo: ')))
saque = float((input('Digite quanto deseja sacar: ')))

status = 'Saque realizado com Sucesso' if saldo >= saque else 'Não foi possivel sacar, tente um valor menor que o saldo!'

print(f'{status}')