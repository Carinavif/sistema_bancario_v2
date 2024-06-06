import textwrap

def main(): #função principal
    saldo = 0
    limite = 500
    extrato = ""
    numero_saques = 0
    numero_conta = 1
    contas = []
    usuarios = []
    LIMITE_SAQUES = 3
    AGENCIA = "0001"

    while True:

        opcao = input(menu())

        if opcao == "d":
            valor = float(input("Informe o valor do depósito: "))

            if valor > 0:
                saldo += valor
                extrato += f"Depósito: R$ {valor:.2f}\n"
                print(f"Depósito realizado com sucesso no valor de {valor:.2f}\n")

            else:
                print("Operação falhou! O valor informado é inválido.")

        elif opcao == "s":
            valor = float(input("Informe o valor do saque: "))

            excedeu_saldo = valor > saldo

            excedeu_limite = valor > limite

            excedeu_saques = numero_saques >= LIMITE_SAQUES

            if excedeu_saldo:
                print("Operação falhou! Você não tem saldo suficiente.")

            elif excedeu_limite:
                print("Operação falhou! O valor do saque excede o limite.")

            elif excedeu_saques:
                print("Operação falhou! Número máximo de saques excedido.")

            elif valor > 0:
                saldo -= valor
                extrato += f"Saque: R$ {valor:.2f}\n"
                numero_saques += 1
                print(f"Saque realizado com sucesso no valor de {valor:.2f}\n")

            else:
                print("Operação falhou! O valor informado é inválido.")

        elif opcao == "e":
            print("\n================ EXTRATO ================")
            print("Não foram realizadas movimentações." if not extrato else extrato)
            print(f"\nSaldo: R$ {saldo:.2f}")
            print("==========================================")

        elif opcao == "nu":
            criar_usuario(usuarios)

        elif opcao == "nc":
            numero_conta = len(contas) +1
            conta = criar_conta(AGENCIA, numero_conta, usuarios)
            
            if conta:
                contas.append(contas)

        elif opcao == "lc":
            listar_contas(contas)
             
        elif opcao == "q":
            print("Obrigado por ser nosso cliente, tenha um bom dia.")
            break

        else:
            print("Operação inválida, por favor selecione novamente a operação desejada.")

def menu(): #função que chama o menu principal
    menu = """\n
    ========== MENU ==========
    [d]\t Depositar
    [s]\t Sacar
    [e]\t Extrato
    [nu]\t Novo usuário
    [nc]\t Nova Conta
    [lc]\t Listar Contas
    [q]\t Sair
    => """
    return textwrap.dedent(menu)

def sacar(*, saldo, valor, extrato, limite, numero_saques, limite_saques):
    excedeu_saldo = valor > saldo
    excedeu_limite = valor > limite
    excedeu_saques = numero_saques >= limite_saques

    if excedeu_saldo:
        print("\n Operação não pôde ser concluída. Você não possui saldo suficiente.")

    elif excedeu_limite: 
        print("\n Operação não pôde ser concluída. O valor excede o limite diário.")

    elif excedeu_saques:
        print("\n Operação não pôde ser concluída. Você já realizou o número máximo de saques diários permitidos. Tente novamente mais tarde.")

    elif valor > 0:
        saldo -= valor
        extrato += f"Saque:\t\tR$ {valor:.2f}\n"
        numero_saques += 1
        print("\n Saque realizado com sucesso! Obrigado e volte sempre.")

    else:
        print("\n Operação não pôde ser concluída")
    
    return saldo, extrato, numero_saques

def exibir_extrato(saldo, /, *, extrato): #Positionaland keywod only.
    print("\n================ EXTRATO ================")
    print("Não foram realizadas movimentações." if not extrato else extrato)
    print(f"\nSaldo: R$ {saldo:.2f}")
    print("==========================================")

def filtrar_usuario(cpf, usuarios):
    usuarios_filtrados = [usuario for usuario in usuarios if usuario["cpf"] == cpf]
    return usuarios_filtrados[0] if usuarios_filtrados else None

def criar_usuario(usuarios):
    cpf = input("Informe o CPF (Somente números): ")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print("\n Esse CPF já está cadastrado.")
        return
    
    nome = input("Informe o seu nome completo:")
    data_nascimento = input("Informe a data de nascimento (dd-mm-aaaa)")
    endereco = input("Informe seu endereço (logradouro, numero - bairro - cidade/sigla estado): ")

    usuarios.append({"nome": nome, "data_nascimento": data_nascimento, "cpf": cpf, "endereco": endereco})

    print(" === Usuário criado com sucesso! === ")

def criar_conta(agencia, numero_conta, usuarios):
    cpf = input("Informe o CPF do usuário: ")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print("\n === Conta criada com sucesso! ===")
        return {"agência": agencia, "numero_conta": numero_conta, "usuario": usuario}
    
    print ("\n Usuário não encontrado, fluxo de criação de conta encerrado.")

def listar_contas(contas):
    for conta in contas:
        linha = f"""\
            Agência:\t{conta['agencia']}
            C/C:\t\t{conta['numero_conta']}
            Titular:\t{conta['usuario']['nome']}
        """
        print("=" * 100)
        print(textwrap.dedent(linha))

main()