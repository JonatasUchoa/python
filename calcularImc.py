def calcularImc(massa,tamanho):
    return massa/(tamanho**2)

print("Calculadora de imc,calcule sem dor de cabeça!!!")
print("")
peso = float(input("digite o seu peso atual:\n"))
altura = float(input("digite sua altura, separando os decimais por ponto ' . '\n"))

imc = calcularImc(peso,altura)

if imc < 18.5:
    print("MAGREZA, seu imc é: {:.2f}".format(imc))
elif 18.5 <= imc <= 24.9:
    print("NORMAL, seu imc é:{:.2f}".format(imc))
elif 25.0 <= imc <= 29.9:
    print("SOBREPESO,obesidade grau 1,seu imc é:{:.2f}".format(imc))
elif 30.0 <= imc <= 39.9:
    print("OBESIDADE grau 2,seu imc é:{:.2f}".format(imc))
elif imv >= 40:
    print("OBESIDADE GRAVE grau 3,seu imc é:{:.2f}".format(imc))
else:
    print("digite os dados corretamente,somente números e separados por ponto ' . '")



