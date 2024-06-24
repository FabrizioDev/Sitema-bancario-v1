usuario = "Teste"
saldo = 0.00
total_saques = 3
limite_saque = 500
limite_saque_total = 1500
DEPOSITOS_REALIZADOS = []
SAQUES_REALIZADOS = []

def exibir_extrato():
    print(f'''
    ======== EXTRATO ========
    
    Depositos Realizados:
    ''')
    if DEPOSITOS_REALIZADOS:
        for deposito in DEPOSITOS_REALIZADOS:
            print(f"- R$ {deposito:.2f}")
    else:
        print("Nenhum depósito realizado.")

    print(f'''
    Saques Realizados:
    ''')
    if SAQUES_REALIZADOS:
        for saque in SAQUES_REALIZADOS:
            print(f"- R$ {saque:.2f}")
    else:
        print("Nenhum saque realizado.")

    print(f'''
    Saldo:
    {saldo}
    ======================
    ''')
    voltar = input("Voltar à conta? [Y/N]: ")
    if voltar.upper() == "Y":
        exibir_menu()
    else:
        print("Saindo do extrato...")

def sacar(valor):
    global saldo, total_saques
    if valor > 0 and valor <= limite_saque:
        if saldo >= valor:
            saldo -= valor
            total_saques -= 1
            SAQUES_REALIZADOS.append(valor)
            print(f"R$ {valor} sacado com sucesso!")
            exibir_menu()
        else:
            print("Saldo insuficiente!")
            exibir_menu()
    elif valor <= 0:
        print(f"Valor inválido: R$ {valor}")
        sacar(float(input("Quanto deseja sacar? R$ ")))
    else:
        print(f"O limite de saque é de R$ {limite_saque:.2f}")
        sacar(float(input("Quanto deseja sacar? R$ ")))

def depositar(valor):
    global saldo
    if valor > 0:
        saldo += valor
        DEPOSITOS_REALIZADOS.append(valor)
        print(f"R$ {valor} depositado com sucesso!")
        exibir_menu()
    elif valor <= 0:
        print(f"Valor inválido: R$ {valor}")
        depositar(float(input("Quanto deseja depositar? R$ ")))
    else:
        print("Ação inválida!")
        depositar(float(input("Quanto deseja depositar? R$ ")))

def exibir_menu():
    status_conta = "Saldo disponível para saque" if saldo > 0 else "Não é possível sacar dinheiro, por falta de saldo"
    pode_sacar = saldo > 0
    opcao = int(input(f'''
    =============== CONTA ===============
                       
    Bem-vindo à sua conta, seu saldo é:
    R$ {saldo:.2f}
    
    - {status_conta}
    - {total_saques} saques disponíveis

    O que deseja fazer?

    1 - Sacar Dinheiro
    2 - Depositar Dinheiro
    3 - Ver Extrato
    0 - Sair
      
    =====================================
    Escolha: '''))

    if opcao == 1:
        if pode_sacar and total_saques > 0:
            sacar(float(input("Quanto deseja sacar? R$ ")))
        elif not pode_sacar:
            print("Não há saldo! Deposite.")
            exibir_menu()
        else:
            print("Limite de saques diários atingido!")
            exibir_menu()
    elif opcao == 2:
        depositar(float(input("Quanto deseja depositar? R$ ")))
    elif opcao == 3:
        exibir_extrato()
    elif opcao == 0:
        print("Saindo...")
    else:
        print("Ação inválida!")
        exibir_menu()

exibir_menu()
