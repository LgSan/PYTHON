saldo_atual = 0

depositar = int(input('Informe o valor:'))

sacar = int(input('Informe o valor:'))

saldo_atual = depositar +(- sacar)

print(saldo_atual)

if saldo_atual < 0 :

    print('Seu saldo atual é', saldo_atual,'Vc usará o cheque especial')
else:
    print('Operação concluida')
    