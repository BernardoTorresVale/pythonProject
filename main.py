'''
Exercicio ppra descobrir se o numero é par ou nao
'''


def par(numero):
    num = numero % 2
    if num == 0:
        return True
    else:
        return False


if __name__ == '__main__':
    name = input('como te chamas? ')
    continuar = 's'
    while continuar == 's':
        num = int(input('insira um numero '))
        if par(num):
            print(f'0 numero {num} é par')
        else:
            print(f'0 numero {num} é impar')
        continuar = input('repetir [s, n]? ')
    print(f'Adeus {name}! ')
