def carro_completo(nome, marca, /, ano, *, cor):
    completo = print(f'O nome do carro é{nome}, A marca do carro é do carro: {marca}, O ano do carro: {ano}, A cor do carro é: {cor}')
    return completo

nome_c = str(input('Digite o nome do carro: '))
modelo_c = str(input("Digite a MArca do carro: "))
ano_c = int(input('Digite o ano do carro: '))
cor_carro_v = str(input('Digite a cor do carro: '))
carro_completo(nome_c, modelo_c, ano_c, cor = cor_carro_v)
