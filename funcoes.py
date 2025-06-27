from decimal import Decimal


# Criar usuário
def criarUsuario():

    usuario = {}

    print("Insira as informações solicitadas:\n")
    usuario["Nome"] = input("Nome completo: ")
    usuario["Data de nascimento"] = input("Data de nascimento (dd/MM/aaaa): ")
    usuario["CPF"] = input("CPF (apenas números): ")
    logradouro = input("Rua: ")
    numero = input("Nº: ")
    bairro = input("Bairro: ")
    cidade = input("Cidade: ")
    estado = input("Estado (sigla): ")
    usuario["Endereço"] = f"{logradouro}, {numero} - {bairro} - {cidade}/{estado}"

    return usuario


# Criar conta conrrente
def criarContaCorrente(base_numero_conta, usuario_vinculado):

    conta = {}

    conta["Agencia"] = "0001"
    conta["Numero da conta"] = base_numero_conta + 1
    conta["Usuario"] = usuario_vinculado
    conta["Saldo"] = Decimal(0)
    conta["Saques"] = []
    conta["Depositos"] = []

    return conta


# Depositar
def depositar(saldo, valor, lista_depositos):

    if valor <= 0:
        print("\nFalha ao tentar realizar depósito. O valor depositado deve ser maior do que zero.")
    else:
        saldo = saldo + valor
        lista_depositos.append(valor)
        print("\nDepósito realizado com sucesso.")

    return saldo, lista_depositos


# Sacar
# Dúvidas: de onde vem a info do numero_saques? e de saldo? e o valor? como chamar extrato() e usar lista_saques nela?
def sacar(saldo, valor, numero_saques, lista_saques, LIMITE=500, LIMITE_SAQUES=3):

    if numero_saques < LIMITE_SAQUES:        
        if valor <= 0:
            print("\nFalha ao tentar realizar saque. O valor sacado deve ser maior do que zero.")
        elif valor > LIMITE:
            print("\nFalha ao tentar realizar saque. O valor que você está tentando sacar é maior do que o limite permitido. Tente sacar um valor menor.")
        else:
            if valor <= saldo:
                saldo = saldo - valor
                lista_saques.append(valor)
                print("\nSaque realizado com sucesso.")
            else:
                print("\nFalha ao tentar realizar saque. Não é possível completar a operação por falta de saldo.")
    else:
        print("\nFalha ao tentar realizar saque. Você atingiu a quantidade máxima de saques do dia.")

    return saldo, lista_saques

# Verificar extrato
def extrato(saldo, extrato="???"):
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