from decimal import Decimal
from datetime import datetime
import re


# Criar usuário
def criarUsuario():

    usuario = {}

    print("Insira as informações solicitadas:\n")
    usuario["Nome"] = input("Nome completo: ")
    data_nascimento_raw = input("Data de nascimento (dd/MM/aaaa): ")
    try:
        usuario["Data de nascimento"] = datetime.strptime(data_nascimento_raw, "%d/%m/%Y")
        data_valida = True
    except ValueError:
        print("Operação falhou: a data deve obedecer o formato dd/MM/aaaa.")
        data_valida = False
    if data_valida:
        cpf_raw = input("CPF (apenas números): ")
        usuario["CPF"] = re.sub(r'\D', '', cpf_raw)
        if len(usuario["CPF"]) != 11:
            print("Operação falhou: o CPF digitado é inválido.")
            return False
        else:
            logradouro = input("Rua: ")
            numero = input("Nº: ")
            bairro = input("Bairro: ")
            cidade = input("Cidade: ")
            estado = input("Estado (sigla): ")
            usuario["Endereço"] = f"{logradouro}, {numero} - {bairro} - {cidade}/{estado}"
            return usuario


# Criar conta corrente
# Todos os argumentos são posicionais
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
# Todos os argumentos são posicionais
def depositar(saldo, valor, lista_depositos):

    if valor <= 0:
        print("\nFalha ao tentar realizar depósito. O valor depositado deve ser maior do que zero.")
    else:
        saldo = saldo + valor
        lista_depositos.append(valor)
        print("\nDepósito realizado com sucesso.")

    return saldo, lista_depositos


# Sacar
# Todos os argumentos são nomeados
def sacar(*, saldo, valor, numero_saques, lista_saques, LIMITE=500, LIMITE_SAQUES=3):

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
# Argumentos posicionais: saldo // Argumentos nomeados: lista_depositos e lista_saques
def extrato(saldo, /, *, lista_depositos, lista_saques):

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

    return None