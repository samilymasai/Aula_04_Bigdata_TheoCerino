compra = float(input('Qual seu valor:'))
pagamento = input('Forma de pagamento á vista ou parcelado:').lower()
if compra > 250 and pagamento == "á vista":
    desconto = compra * 84/100
    print(f'Com desconto com o valor {desconto}')
else: 
     print(f'Sem desconto com o valor  {compra}')
