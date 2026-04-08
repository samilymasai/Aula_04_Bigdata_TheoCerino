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

# Operadores AND e OR
usuario = input('Nome: ')
senha = input( 'Senha: ')
if usuario == "admin" and senha == "1234":
    print('login realizado com sucesso') 
else:
    print('Usuário ou senha incorreto')