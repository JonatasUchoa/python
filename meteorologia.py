#progama deve receber as temperaturas registradas e imprimir a temperatura arredondada mínima e a máxima e a média

def media(quantidadeTemperatura,somaTemperatura):
    return somaTemperatura/quantidadeTemperatura

numeroTemperatura = int(input("digite o número de temperaturas registradas: "))

soma = temperaturaMinima = temperaturaMaxima = float(input("digite a temperatura 1: "))
temperaturaAtual = 0

for temperatura in range(2,numeroTemperatura+1):
    temperaturaAtual = float(input("digite a temperatura:%.f: "%temperatura))
    soma += temperaturaAtual
    if temperaturaAtual > temperaturaMaxima:
        temperaturaMaxima = temperaturaAtual
    if temperaturaAtual < temperaturaMinima:
        temperaturaMinima = temperaturaAtual
print("\nA máxima foi:",round(temperaturaMaxima),"°C","\na mínima foi:",round(temperaturaMinima),"°C","\na média foi:",round(media(numeroTemperatura,soma)),"°C")

