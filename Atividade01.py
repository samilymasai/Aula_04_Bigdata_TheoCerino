compra = int(input('Qual foi valor da sua compra ?: '))
if compra > 250:
    desconto = compra * 84/100
    print(f'Com desconto com o valor {desconto} ')
else:
    print(f'Sem desconto com o valor  {compra}')
    

