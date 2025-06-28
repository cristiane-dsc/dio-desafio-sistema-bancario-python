from decimal import Decimal
import funcoes as f

menu = """

[u] Cadastrar novo usuário
[c] Criar conta corrente
[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> """

usuarios = {}
contas_correntes = {}

boas_vindas = """
Bem vinda(o) ao nosso novo sistema bancário!
Qual operação você deseja realizar?"""

print(boas_vindas)

while True:

    opcao = input(menu)

    if opcao == "u":
        print("Cadastrar novo usuário\n")
        usuario = f.criarUsuario()
        if usuario:
            cpf = usuario["CPF"]
            if cpf in usuarios:
                print("Operação falhou: já existe um usuário cadastrado com o mesmo CPF.")
            else:
                usuarios[cpf] = usuario
                print("Usuário cadastrado com sucesso")

    elif opcao == "c":
        print("Criar conta corrente\n")
        tamanho_lista_contas = len(contas_correntes)
        cpf_usuario = input("Digite o CPF do usuário que deve ser vinculado à conta: ")
        if cpf_usuario not in usuarios:
            print("Operação falhou: não é possível vincular o usuário à conta porque ele não existe em nossa base de dados.")
        else:
            conta = f.criarContaCorrente(tamanho_lista_contas, cpf_usuario)
            numero_conta = conta["Numero da conta"]
            contas_correntes[numero_conta] = conta
            print("Conta criada com sucesso")
    
    elif opcao == "d":
        print("Depósito")
        conta_deposito = int(input("\nConta para depósito\n=> "))
        if conta_deposito in contas_correntes:
            saldo_conta_deposito = contas_correntes[conta_deposito]["Saldo"]
            valor_deposito = Decimal(input("Informe o valor que você deseja depositar\n=> "))
            depositos = contas_correntes[conta_deposito]["Depositos"]
            saldo_conta_deposito, depositos = f.depositar(saldo_conta_deposito, valor_deposito, depositos)
            contas_correntes[conta_deposito]["Saldo"] = saldo_conta_deposito
            contas_correntes[conta_deposito]["Depositos"] = depositos
        else:
            print("Operação falhou: a conta corrente informada não existe.")

    elif opcao == "s":
        print("Saque")
        conta_saque = int(input("\nConta para saque\n=> "))
        if conta_saque in contas_correntes:
            saldo_saque = contas_correntes[conta_saque]["Saldo"]
            valor_saque = Decimal(input("\nInforme o valor que você deseja sacar\n=> "))
            numero_saques = len(contas_correntes[conta_saque]["Saques"])
            saques = contas_correntes[conta_saque]["Saques"]
            saldo_saque, saques = f.sacar(saldo=saldo_saque, valor=valor_saque, numero_saques=numero_saques, lista_saques=saques)
            contas_correntes[conta_saque]["Saldo"] = saldo_saque
            contas_correntes[conta_saque]["Saques"] = saques
        else:
            print("Operação falhou: a conta corrente informada não existe.")

        
    elif opcao == "e":
        print("Extrato")
        conta_extrato = int(input("\nConta\n=> "))
        if conta_extrato in contas_correntes:
            saldo_extrato = contas_correntes[conta_extrato]["Saldo"]
            saques_extrato = contas_correntes[conta_extrato]["Saques"]
            depositos_extrato = contas_correntes[conta_extrato]["Depositos"]
            f.extrato(saldo_extrato, lista_depositos=depositos_extrato, lista_saques=saques_extrato)
        else:
            print("Operação falhou: a conta corrente informada não existe.")

    elif opcao == "q":
        break

    else:
        print("\nOperação inválida. Por favor, selecione novamente a operação desejada.")