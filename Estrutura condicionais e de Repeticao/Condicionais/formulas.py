def cnh(ida):
    maior_idade = 18
    idade_especial = 16

    if ida >= maior_idade:
        print('Você pode tirar a CNH')

    elif ida < maior_idade and ida >= idade_especial:
        print(' Você pode assistir aulas teoricas, mas não pode realizar as aulas práticas!')

    else:
        print('Você não tem idade suficiente para tirar a carteir   a')
