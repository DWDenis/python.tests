menu = '''
[d]  Deposito
[s]  Saque
[e]  Extrato
[q] Sair

=> '''

d_valor= 0
s_valor = 0

#precisa ser positivo
def Deposito():
    global d_valor 
    d_valor = int(input("Qual o valor que deseja depositar: "))
    if d_valor < 2:
        print("O valor de deposito precisa ser maior que 2")
    return print(f"Um deposito foi realizado no valor de R$ {d_valor}")


# max de 500
# limite 3 por dia
def Saque():
    global s_valor, d_valor
    print(f"O valor disponivel e de: {d_valor}")
    
    i = 0
    while i <= 2:
        s_valor = int(input("Qual o valor do saque: "))
        
        if s_valor > 500:
            print("Limite de saque diaria de [R$ 500.00]")
        elif s_valor > d_valor:
            print(f"Valor disponivel {d_valor}")
        else:
            d_valor -= s_valor
            print(f"O saldo atual e de: R$ {d_valor}")
        
        outro_saque = input("Deseja realizar mais um saque? s/n =>  ")
        if outro_saque == 'n':
            break
        
        i += 1




# Deve retornar o valor atual apos operacoes
# valor deve ser exibido no formato R$ com "." para separacao de decimais
def Extrato():
    global d_valor, s_valor
    extrato_atual = d_valor - s_valor
    print(f"O extrato atual e de: R$ {extrato_atual:.2f}")


while True:
    resposta = input("Ola, por gentileza escolher umas das opcoes abaixo: " + menu) 

    if resposta == "d":
        Deposito()
    elif resposta == "s":
        Saque()
    elif resposta == "e":
        Extrato()
    elif resposta == "q":
        print("Tenha um bom dia!")
        break


