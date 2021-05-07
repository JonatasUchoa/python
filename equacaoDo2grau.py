#para esse progama so será levado em conta equacões do 2grau completas

a = int(input("digite o valor de a:\n"))
b = int(input("digite o valor de b:\n"))
c = int(input("digite o valor de c:\n"))

if a != 0 or b != 0 or c != 0:
    delta = b**2 - 4*a*c
    if delta >= 0:
        raizXpositivo = (-b + (delta**(1/2)))/(2*a)
        raizXnegativo = (-b - (delta**(1/2)))/(2*a)
        print("x1:",raizXpositivo,"| x2:",raizXnegativo)
    else:
        print("delta não pode ser menor que zero")
else:
    print("a ou b ou c não podem ser zero pois só será calculado equações completas")