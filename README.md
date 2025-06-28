<h1>
    <a href="https://www.dio.me/">
     <img align="center" width="40px" src="https://hermes.digitalinnovation.one/assets/diome/logo-minimized.png"></a>
    <span> Criando um Sistema Bancário com Python</span>
</h1>

Este projeto é um desafio da trilha de Fundamentos do bootcamp **Santander 2025 - Back-End com Python**, oferecido pela DIO e no qual fui bolsista. Trata-se de uma experiência prática de desenvolvimento de software financeiro dividido em fases.

## Fase 1

Na 1a fase, os participantes puderam desenvolver um sistema para depósitos e saques, com consulta de extrato bancário. 

## ⚙️ Funcionalidades - Fase 1

**Operação de depósito:**
- É possível depositar apenas valores positivos.
- A V1 do projeto trabalha apenas com 1 usuário e não é necessário identificar agência nem conta bancária.
- Todos os depósitos devem ser armazenados em uma variável e exibidos na operação de extrato.

**Operação de saque:**
- Limite de 3 saques por dia.
- Limite de R$ 500,00 por saque.
- Caso o usuário não tenha saldo suficiente para realizar o saque, o sustema deve exibir uma mensagem informando que não é possível sacar o dinheiro por falta de saldo.
- Todos os saques devem ser armazenados em uma variável e exibidos na operação de extrato.

**Operação de extrato:**
- Deve listar todas as movimentações de depósitos e saques.
- Deve exibir o saldo atual da conta no final da listagem.
- Os valores devem ser exibidos no formato R$ xxx.xx.

<br>

> Apesar de haver uma solução apresentada no conteúdo da trilha, eu desenvolvi minha própria solução de forma independente, utilizando apenas o template inicial fornecido pelo instrutor. A partir disso, elaborei o sistema da forma que considerei mais adequada.

## Fase 2

Na 2a fase, o sistema teve as funcionalidades separadas em funções, além de ganhar 2 novas operações.

### ✨ Novas funcionalidades - Fase 2

**Criar usuário:**
- O programa deve armazenar os usuários em uma lista.
- Um usuário é composto por noma, data de nascimento, CPF e endereço.
- O endereço é uma string com formato: logradouro, Nº - bairro - cidade/sigla do estado.
- Apenas os números do CPF devem ser armazenados.
- Não é permitido cadastrar mais de um usuário com o mesmo CPF.

**Criar conta corrente:**
- O programa deve armazenar contas em uma lista.
- Uma conta é composta por agência, número da conta e usuário.
- O número da conta é sequencial, iniciando em 1.
- O número da agência é fixo: 0001.
- O usuário pode ter mais de uma conta, mas uma conta pertence a somente um usuário.
   
<br>

> Assim como na fase 1, existe uma solução apresentada no conteúdo da trilha, porém optei por desenvolver minha própria solução de forma independente, com base no código que desenvolvi da 1a parte. O resultado ficou diferente e menos elegante do que a solução do instrutor, porém foquei em exercitar meu raciocínio e criatividade ao invés de apenas copiar a solução fornecida no curso ou copiar um código de IA.