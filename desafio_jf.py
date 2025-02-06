menu = """

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> """

depositos = []
saques = []
saldo = 0
numero_saques = 0
saques_diarios = 3
limite_saques = 500.00

while True:

    opcao = input(menu)

    if opcao == "d":
        valor = float(input("Informe o valor do depósito: "))

        if valor > 0:
            depositos.append(valor)
            saldo += valor
            print(f'Depósito de R$ {valor:.2f} realizado com sucesso.')

        else:
            print("Operação falhou! O valor informado é inválido.")

    elif opcao == "s":
        valor = float(input("Informe o valor do saque: "))

        if saques_diarios > 0 and valor <= limite_saques and valor <= saldo:
            saques.append(valor)
            saldo -= valor
            saques_diarios -= 1
            print(f'Saque de R$ {valor:.2f} realizado com sucesso.')
        
        elif saques_diarios <= 0:
            print('Limite diário de saques atingido.')
        
        elif valor > limite_saques:
            print('Limite máximo de saque excedido.')
        
        else:
            print('Saldo insuficiente.')

        
    elif opcao == "e":
        
        if not depositos and not saques:
            print(f'Não foram realizadas movimentações.')
        
        else:
            extrato = 'Extrato:\n'
            
            for deposito in depositos:
                extrato += f'Depósito: R$ {deposito:.2f}\n'
            
            for saque in saques:
                extrato += f'Saque: R$ {saque:.2f}\n'
            
            extrato += f'Saldo atual: R$ {saldo:.2f}'
            print(extrato)
        
        
    elif opcao == "q":
        break

    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")
