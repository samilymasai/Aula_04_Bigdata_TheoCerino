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


    # Exemplo IFs
    nota = 10 
    if nota >= 9:
        print('A')
    elif nota >= 7:
        print('B')
    elif nota >= 5:
        print('C')
    elif nota >= 3:
        print('D')
    else: 
        print('E')
    


    # Exemplo IFs
nota = 10 
if nota >= 9:
    print('A')

elif nota >= 7:
    print('B')

elif nota >= 5:
    print('C')

elif nota >= 3:
    print('D')

else: 
    print('E')

# IFs aninhadas 
nota = float(input('insire a nota: '))
frequencia = float(input('informe a frequência: '))

if nota >= 7: 
   # Aprovado por nota, mas precisa checar a frequêcia
    if frequencia >= 75:
     print('Aluno aprovado por nota e a frequência')
    else:
         print('reprovado por frequência baixa')
else: 
    print('Reprovado por nota baixa.')