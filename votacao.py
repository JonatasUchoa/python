#eleção com 3 candidatos deve pedir o número de eletores seu voto e mostrar o resultado parcial para cada eleitor que votar

carlao = 0
pedrao = 0
josefa = 0
numeroEleitores = int(input("digite o número de total de eleitores:\n"))
voto = 0
for i in range(0,numeroEleitores,1):
    voto = int(input("VOTE COM CONSCIÊNCIA!!\ndigite 1 para votar no Carlao, 2 para o Pedrao e 3 para votar na Josefa:\n"))
    if voto == 1:
        carlao += 1
        print("votos: Carlão:",carlao,"| Pedrão:",pedrao, "| Josefa:",josefa)
        print("-")
    elif voto == 2:
        pedrao += 1
        print("votos: Carlão:",carlao,"| Pedrão:",pedrao, "| Josefa:",josefa)
        print("-")
    elif voto == 3:
        josefa +=1
        print("votos: Carlão:",carlao,"| Pedrão:",pedrao, "| Josefa:",josefa)
        print("-")
    else:
        print("digite um número válido")
        print("")
