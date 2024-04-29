def exibir_mensagem(msg):
    print(f'Olá {msg} tudo bem!')


def exibir_idade(ida):
    print(f'Sua idade é {ida}')


def exibir_profissao(pro):
    p = print(f'Sua profissão é {pro}')
    return p


nome = str(input('Digite seu nome: '))
exibir_mensagem(nome)

idade = int(input('Digite sua idade: '))
exibir_idade(idade)

profissao = str(input('Digite sua Profissão: '))
exibir_profissao(profissao)





