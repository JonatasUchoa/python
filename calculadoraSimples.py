def calcular(n1,operation,n2):
    if operation == "+":
        return n1 + n2
    elif operation == "-":
        return n1 - n2
    elif operation == "*":
        return n1 * n2
    elif operation == "/":
        return n1 / n2
    else:
        print("digite um operador válido")
        return

primeiroNumero = float(input("digite o primeiro numero:\n"))
operador = input("digite o operador do calculo:\n")
segundoNumero = float(input("digite o segundo número:\n"))

print(calcular(primeiroNumero,operador,segundoNumero))