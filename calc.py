import os
import msvcrt


def limpa():
    os.system("CLS")


def pausa():
    print('\nPressione qualquer tecla para continuar...\n')
    char = msvcrt.getch()


def soma(a, b):
    c = a + b
    print('Adição\n')
    print(f'Resultado em binário: {c:b}')
    print(f'Resultado em decimal: {c}')


def subtracao(a, b):
    c = a - b
    print('Subtração\n')
    print(f'Resultado em binário: {c:b}')
    print(f'Resultado em decimal: {c}')


def multiplicacao(a, b):
    c = a * b
    print('Multiplicação\n')
    print(f'Resultado em binário: {c:b}')
    print(f'Resultado em decimal: {c}')


def divisao(a, b):
    c = a / b
    print('Divisão\n')
    print(f'Resultado em binário: {c:b}')
    print(f'Resultado em decimal: {c}')


opt = True

while opt is True:
    limpa()
    num_a = int(input('Informe o primeiro valor inteiro: '))
    num_b = int(input('Informe o segundo valor inteiro: '))
    print(f'Primeiro valor em binário: {num_a:b}')
    print(f'Segundo valor em binário: {num_b:b}')
    print('\nSelecione uma operção para realizar com os valores digitados\n')
    print('1 - Adição\n')
    print('2 - Subtração\n')
    print('3 - Multiplicação\n')
    print('4 - Divisão\n')
    print('0 - Sair')
    op = int(input('Selecione uma operação e tecle ENTER: '))
    if op == 1:
        soma(num_a, num_b)
        pausa()
    elif op == 2:
        subtracao(num_a, num_b)
        pausa()
    elif op == 3:
        multiplicacao(num_a, num_b)
        pausa()
    elif op == 4:
        if num_b == 0:
            print('Impossível dividir por 0')
            pausa()
        else:
            divisao(num_a, num_b)
            pausa()
    elif op == 0:
        print('Operação finalizada pelo usuário.')
        pausa()
        opt = False
    else:
        print('Opção inválida.')
        pausa()
