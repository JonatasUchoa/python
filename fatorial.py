def fatorial(numero,somatorio,numeroInicial):
    somatorio = numeroInicial*numero
    numero=numero-1
    while numero > 0:
        somatorio = somatorio*numero
        numero=numero-1
    print(somatorio)

numeroFatoracao = int(input("digite um numero para a operação de fatoração:\n"))
soma = 0
numeroInicial = numeroFatoracao
numeroFatoracao=numeroFatoracao-1
fatorial(numeroFatoracao,soma,numeroInicial)


