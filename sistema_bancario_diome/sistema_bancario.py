"""
Unico usuário

Operações:
    depósito
        Valores positivos
    saque
        Limite de 3 saques diários
        Limite no valor do saque de R$ 500,00
        Não havendo saldo, retornar uma msg informando que não há saldo para o saque
    extrato
        Todos os depositos e saques devem aparecer no retorno do extrato
        Ao final do extrato deve aparecer o saldo
        Se tiver em branco retornar 'Não foram realizadas movimentações.'

    Formato:
        R$ XXX.XX
"""

menu = """
[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair
"""

saldo = 0
limite_saque = 500
extrato = []
numero_saques = 0
LIMITE_SAQUES = 3


def numero_positivo(num: float) -> bool:
    """Função verifica se o número é positivo.

    Args:
        num (float): _description_

    Returns:
        bool: _description_
    """
    if num > 0:
        return True
    else:
        False


while True:
    opcao = input(menu)

    if opcao == 'd':
        deposito = float(input('Valor do deposito: '))
        if numero_positivo(deposito):
            saldo += deposito
            extrato.append(deposito)
            print(f'{deposito} reais depositados')
        if not numero_positivo(deposito):
            print('Depositos devem ser números positivos')
            continue

    if opcao == 's':
        numero_saques += 1
        if numero_saques > LIMITE_SAQUES:
            print('Sque não permitito. Limite de três saques diários.')
            continue
        else:
            valor_saque = float(input('Valor do saque: '))
            if valor_saque > limite_saque:
                print('Saque indisponivel. Valor solicitado maior que o permitido.')
            if valor_saque > saldo:
                print('Saldo indisponivel.')
            else:
                saldo -= valor_saque
                extrato.append(-valor_saque)
    if opcao == 'e':
        if not extrato:
            print('Não foram realizadas movimentações.')
            continue
        [print(f'R$ {v:.2f}') for v in extrato]
        print(f'Saldo: R$ {sum(extrato)}')

    if opcao == 'q':
        break
