def es_primo(numero):
    contador = 0
    for i in range(1, numero + 1):
        if numero % i == 0:
            contador = contador + 1
        else:
            continue
    if contador > 2 or contador == 1:
        return False
    else:
        return True


def run():
    numero = int(input('Ingrese el número a evaluar: '))
    if es_primo(numero):
        print(f'El número {numero} es primo')
    else:
        print(f'El número {numero} no es primo.')


if __name__ == '__main__':
    run()