from decimal import Decimal
from funcoes import criarUsuario, criarContaCorrente, depositar, sacar

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
#saldo = 0
limite_valor_saque = 500
#extrato = ""
#numero_saques = 0
LIMITE_SAQUES = 3

boas_vindas = """
Bem vinda(o) ao nosso novo sistema bancário!
Qual operação você deseja realizar?"""

print(boas_vindas)

while True:

    opcao = input(menu)

    if opcao == "u":
        print("Cadastrar novo usuário\n")
        usuario = criarUsuario()
        cpf = usuario["CPF"]
        if cpf in usuarios:
            print("Operação falhou: já existe um usuário cadastrado com o mesmo CPF.")
        else:
            usuarios[cpf] = usuario
            print("Usuário cadastrado com sucesso")
            print(usuarios)

    elif opcao == "c":
        print("Criar conta corrente\n")
        tamanho_lista_contas = len(contas_correntes)
        cpf_usuario = input("Digite o CPF do usuário que deve ser vinculado à conta: ")
        if cpf_usuario not in usuarios:
            print("Operação falhou: não é possível vincular o usuário à conta porque ele não existe em nossa base de dados.")
        else:
            conta = criarContaCorrente(tamanho_lista_contas, cpf_usuario)
            numero_conta = conta["Numero da conta"]
            contas_correntes[numero_conta] = conta
            print("Conta criada com sucesso")
            print(contas_correntes)
    
    elif opcao == "d":
        print("Depósito")
        conta_beneficiario = int(input("\nConta para depósito\n=> "))
        if conta_beneficiario in contas_correntes:
            saldo_conta_beneficiario = contas_correntes[conta_beneficiario]["Saldo"]
            valor_deposito = Decimal(input("Informe o valor que você deseja depositar\n=> "))
            depositos = contas_correntes[conta_beneficiario]["Depositos"]
            saldo_conta_beneficiario, depositos = depositar(conta_beneficiario, saldo_conta_beneficiario, valor_deposito, depositos)
            contas_correntes[conta_beneficiario]["Saldo"] = saldo_conta_beneficiario
            contas_correntes[conta_beneficiario]["Depositos"] = depositos
        else:
            print("Operação falhou: a conta corrente informada não existe.")

    elif opcao == "s":
        print("Saque")
        conta = int(input("\nConta para saque\n=> "))
        saldo = contas_correntes[conta]["Saldo"]
        print(f"Saldo antes: {saldo}")
        valor_saque = Decimal(input("\nInforme o valor que você deseja sacar\n=> "))
        numero_saques = len(contas_correntes[conta]["Saques"])
        print(f"Numero de saques antes: {numero_saques}")
        saques = contas_correntes[conta]["Saques"]
        print(f"Lista de saques antes: {saques}")
        saldo, saques = sacar(saldo=saldo, valor=valor_saque, numero_saques=numero_saques, lista_saques=saques)
        contas_correntes[conta]["Saldo"] = saldo
        contas_correntes[conta]["Saques"] = saques
        print(f"Número de saques depois: {len(contas_correntes[conta]['Saques'])}")
        print(f"Saldo depois: {saldo}")
        print(f"Lista de saques depois: {saques}")

        
    elif opcao == "e":
        print("Extrato")

    elif opcao == "q":
        break

    else:
        print("\nOperação inválida. Por favor, selecione novamente a operação desejada.")