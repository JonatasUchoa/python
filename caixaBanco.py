#so pode saque de 10 a 600

print("olá! bem vindo ao caixa banco two")

valorSaque = int(input("digite o valor a do saque:\n"))

quant100 = 0
quant50 = 0
quant10 = 0
quant5 = 0
quant1 = 0

saqueVariavel = valorSaque

if 10 <= valorSaque <= 600:
    if valorSaque > 100:
        quant100 = valorSaque // 100
        saqueVariavel = valorSaque-100*quant100
    if saqueVariavel > 50:
        quant50 = saqueVariavel // 50
        saqueVariavel = saqueVariavel-50*quant50
    if saqueVariavel > 10:
        quant10 = saqueVariavel // 10
        saqueVariavel = saqueVariavel-10*quant10
    if saqueVariavel > 5:
        quant5 = saqueVariavel // 5
        saqueVariavel = saqueVariavel-5*quant5
    if saqueVariavel > 0:
        if saqueVariavel % 1 != 0:
            quant1 = (saqueVariavel // 1)+1
        else:
            quant1 = saqueVariavel // 1 
    print("ao sacar ",valorSaque," reais","receberá",quant100,"notas de 100 |",quant50,"notas de 50 |",quant10,"notas de 10 |",
    quant5,"notas de 5 |",quant1,"notas de 1 ") 
        
else:
    print("você só pode sacar de 10 a 600 reais")

