def calculoSalario(param1,param2):
    return param1 * param2

tempoTrabalhado = float(input("digite quantas horas você trabalhou:\n"))
salario = float(input("digite quanto você ganha por hora:\n"))


print("você deve receber:",calculoSalario(salario,tempoTrabalhado))
