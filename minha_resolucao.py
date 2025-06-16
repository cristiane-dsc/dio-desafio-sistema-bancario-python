from decimal import Decimal

menu = """

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3
valor_deposito = 0
lista_depositos = []
valor_saque = 0
lista_saques = []

boas_vindas = """
Bem vinda(o) ao nosso novo sistema bancário!
Qual operação você deseja realizar?"""

print(boas_vindas)

while True:

    opcao = input(menu)

    if opcao == "d":
        print("Depósito")

        valor_deposito = Decimal(input("\nInforme o valor que você deseja depositar\n=> "))
        if valor_deposito <= 0:
            print("\nO valor depositado deve ser maior do que zero.")
        else:
            saldo = saldo + valor_deposito
            lista_depositos.append(valor_deposito)
            print("\nDepósito realizado com sucesso.")

    elif opcao == "s":
        print("Saque")

        if numero_saques < LIMITE_SAQUES:
            valor_saque = Decimal(input("\nInforme o valor que você deseja sacar\n=> "))
            
            if valor_saque <= 0:
                print("\nO valor sacado deve ser maior do que zero.")
            elif valor_saque > limite:
                print("\nO valor que você está tentando sacar é maior do que o limite permitido. Tente sacar um valor menor.")
            else:
                if valor_saque <= saldo:
                    saldo = saldo - valor_saque
                    lista_saques.append(valor_saque)
                    numero_saques += 1
                    print("\nSaque realizado com sucesso.")
                else:
                    print("\nNão é possível realizar o saque por falta de saldo.")
        else:
            print("\nVocê atingiu a quantidade máxima de saques do dia.")

    elif opcao == "e":
        print("Extrato")

        print("\n"+"Depósitos".center(20,"*")+"\n")
        if len(lista_depositos) == 0:
            print("Não foram realizados depósitos no período")
        else:
            for deposito in lista_depositos:
                print(f"R$ {deposito: .2f}")
        
        print("\n"+"Saques".center(20,"*")+"\n")
        if len(lista_saques) == 0:
            print("Não foram realizados saques no período")
        else:
            for saque in lista_saques:
                print(f"R$ {saque: .2f}")

        print("\n"+"Saldo".center(20,"*")+"\n")
        print(f"R$ {saldo: .2f}")       

    elif opcao == "q":
        break

    else:
        print("\nOperação inválida. Por favor, selecione novamente a operação desejada.")