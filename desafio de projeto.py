import os 
os.system('cls')

saldo = 0
limite = 500
extrato = ""
num_saques = 0
LIMITE_SAQUES = 3


while True:
    print("Informe a operação desejada \n 1- Depósito;\n 2- Saque ;\n 3- Extrato;\n 0- Sair;")
    operacao = int(input("\n Digte:"))
    if operacao == 0:
        print("Obrigado por utilizar nossos serviços!!")
        break

    elif operacao == 1:
        deposito = float(input("Digite o valor que deseja depositar: "))

        if deposito > 0:
            saldo += deposito
            extrato += f"Depósito: R$ {deposito:.2f}\n"

        else:
            print("Erro na operação!\n Valor informado é invalido")

    elif operacao == 2:
        saque = float(input("Digite o valor que deseja sacar: "))

        saldo_excedido = saque > saldo
        limite_excedido = saque > limite 
        saques_excedidos = num_saques > LIMITE_SAQUES

        if saldo_excedido:
            print("Operação não realizada!\n Saldo insuficiente")

        elif limite_excedido:
            print("Operação não realizada!\n Limite diario excedido")
        
        elif saques_excedidos:
            print("Operação não realizada!\n Limite diario de saques excedido")

        elif saque > 0:
            saldo -= saque
            extrato += f"Depósito: R$ {saque:.2f}\n"
            num_saques += 1

        else:
            print("Erro na operação!\n Valor informado é invalido")

    elif operacao == 3:
        print("\n===== EXTRATO =====")
        print("Não foram realizadas movimentações em sua conta." if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("===================")

    else: 
        print("opreação invalida!\n tente novamente")
        operacao = int(input("Informe a operação desejada \n 1- Depósito;\n 2- Saque ;\n 3- Extrato;\n 0- Sair;"))
    
   



    



    
    
