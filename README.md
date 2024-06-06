# Sistema Bancário

Este é um simples sistema bancário implementado em Python. Ele permite a realização de operações básicas como depósito, saque, consulta de extrato, criação de novos usuários e contas, e a listagem de contas.

## Funcionalidades

- **Depositar**: Permite ao usuário depositar um valor na conta.
- **Sacar**: Permite ao usuário sacar um valor da conta, respeitando o saldo disponível, limite de saque e o número máximo de saques diários.
- **Extrato**: Exibe o extrato das transações realizadas e o saldo atual.
- **Novo Usuário**: Permite a criação de um novo usuário.
- **Nova Conta**: Permite a criação de uma nova conta associada a um usuário existente.
- **Listar Contas**: Lista todas as contas cadastradas.
- **Sair**: Encerra o programa.

## Como Utilizar

1. Execute o script Python.
2. Um menu será exibido com as opções disponíveis.
3. Selecione a opção desejada digitando a letra correspondente e pressionando Enter.

## Estrutura do Código

### Função `main()`
A função principal que contém o loop do menu e gerencia as operações do sistema.

### Função `menu()`
Exibe o menu principal e retorna a opção selecionada pelo usuário.

### Função `sacar()`
Executa a operação de saque, verificando saldo, limite de saque e número máximo de saques diários.

### Função `exibir_extrato()`
Exibe o extrato das transações e o saldo atual.

### Função `filtrar_usuario()`
Filtra um usuário a partir do CPF.

### Função `criar_usuario()`
Cria um novo usuário com os dados fornecidos.

### Função `criar_conta()`
Cria uma nova conta associada a um usuário existente.

### Função `listar_contas()`
Lista todas as contas cadastradas no sistema.

## Requisitos

- Python 3.x

## Executando o Sistema

Para executar o sistema, basta rodar o seguinte comando no terminal:

```bash
python nome_do_arquivo.py
```

## Observações

- Os limites de saque e o número máximo de saques diários são definidos por constantes (`limite` e `LIMITE_SAQUES`).
- A agência é fixa e definida pela constante `AGENCIA`.
- O saldo inicial é zero e pode ser incrementado através de depósitos.

## Exemplo de Uso

```bash
========== MENU ==========
[d]    Depositar
[s]    Sacar
[e]    Extrato
[nu]   Novo usuário
[nc]   Nova Conta
[lc]   Listar Contas
[q]    Sair
=> d
Informe o valor do depósito: 1000
Depósito realizado com sucesso no valor de 1000.00
```

---
