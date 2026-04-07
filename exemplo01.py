# Estrutura if
idade = int(input(' Insire a idade: '))

if idade >= 18:
    print('Voçê é adulto')
else:
    print('Voçê não é adulto')
    #-------------------------------------------

    pontos = int(input(' Informe os pontos: '))
    if pontos >= 100: 
        print('Excelente!')
    elif pontos >= 50:
        print('Bom desempenho!')
    elif pontos >= 25:
        print('Satisfatório.')
    else:
        print('Pratique mais.')