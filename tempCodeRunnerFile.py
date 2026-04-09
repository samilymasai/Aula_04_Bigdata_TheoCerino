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