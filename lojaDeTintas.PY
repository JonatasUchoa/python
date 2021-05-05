# 1L de tinta cobre 6m^2


print("BEM VINDO!,aqui na Norte tintas você pode calcular o preço de e o valor exato de tinta que você precisará")

area = float(input("digite a área que deve ser pintada:\n"))

litros = area / 6
if litros % 6 !=0:
    litros= (area//6)+1

preco18 = 80
preco4 = 25
quantidade4 = 0
quantidade18=0
precoTotal=0
if litros >= 18:
  quantidade18 = litros // 18
  precoTotal = quantidade18*preco18
  litros=litros-(quantidade18*18)
  if litros != 0:
    if litros % 4 != 0 :
     quantidade4 = (litros // 4)+1
     precoTotal = precoTotal + (quantidade4*preco4)
else:
    quantidade4 = (litros // 4)+1
    precoTotal = precoTotal + (quantidade4*preco4)
print("a quantidade de latas de 18l é:",quantidade18, "|a quantidade de latas de 4l é:",quantidade4,"|vai custar:",precoTotal)