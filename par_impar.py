# Sistema que verifica se um número informado é par ou ímpar

print('\n\t\t\t-- Verificador de Número Par ou Ímpar')
num = int(input('Informe um número: '))
if num % 2 == 0:
    print(f'{num} é Par')
else:
    print(f'{num} é Ímpar')
