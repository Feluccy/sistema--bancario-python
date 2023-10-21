menu = """

[1] Depositar
[2] Sacar
[3] Extrato
[4] Sair

=> """

saldo = 0
limite = 500
extrato = " "
numero_saques = 0
Limite_Saques = 3 

while True : 
    
    opcao = input(menu)

    if opcao =="1" :
        valor = float (input("Informe o valor do deposito: "))

        if valor > 0:
            saldo += valor
            extrato += f"deposito:R$ {valor :.2f}\n"

        else: 
            print("operacao falhou ! O valor informado e invalido.")    

    elif opcao == "2" :
        valor = float (input("Informe o valor do saque: "))

        excedeu_saldo = valor > saldo 

        excedeu_limite = valor > limite

        excedeu_saques = numero_saques >= Limite_Saques

        if excedeu_saldo:
         print("Operacao falhou! Voce nao tem saldo suficiente.") 

        elif excedeu_limite:
           print("Operacao falhou ! O Valor do saque excede o limite .")

        elif excedeu_saques:
           print("Operacao falhou ! Numero maximo de saques excedido .")  

        elif valor > 0:
         saldo -= valor 
         extrato += f"saque: R$ {valor :.2f}\n"  
         numero_saques += 1

        else :
         print("Operacao falhou ! O Valor informado e invalido.")


    elif opcao == "3" :
        print("\n===========Extrato============")
        print("Nao foram realizadas movimentacoes ." if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo :.2f}")
        print("============================================")

    elif opcao == "4" :
        break   

    else:
        print("Operacao invalida,por favor selecione novamente a operacao desejada.")         
