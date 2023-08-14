saldo = 0.00
limite = 500.00
extrato = ""
quantidadeSaques = 0
limiteSaques = 3

while True:
    menu = int(input( """
    Escolha uma operação:
    [1] Sacar
    [2] Depositar
    [3] Extrato
    [0] Sair
    : """))
    
    if menu == 1:
        valorSaque = float(input("Digite o valor a ser sacado: "))
        if valorSaque > saldo:
            print("O valor a ser sacado é maior do que o disponível em seu saldo")
        elif quantidadeSaques > limiteSaques:
            print("Você já atingiu o limite de saques diários")
        elif valorSaque > 500.00:
                print("O valor máximo permitido por saque é de R$500,00, refaça sua solicitação!") 
        else:
            saldo -= valorSaque
            extrato = f"{extrato}\n-R${valorSaque}"
            quantidadeSaques += 1
    
    elif menu == 2:
        valorDeposito = float(input("Digite o valor a ser depositado: "))
        saldo += valorDeposito
        extrato = f"{extrato}\n+R${valorDeposito}"
        continue
   
    elif menu == 3:
        print(f"""{extrato}
----------------------------
Saldo da conta: R${saldo}""")
    
    elif menu == 0:
        print("Obrigado por utilizar nosso sitema, até breve!")
        break

    else:
        print("Operação inválida, digite novamente")
