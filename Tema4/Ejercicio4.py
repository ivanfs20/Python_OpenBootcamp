"""Opte por hacer una lista, la cual primero se llenara con 100 numeros,
para despues invertir esa lista e imprimir los numeros de forma ascendente"""
count=1
listanumeors=[]

while count<=100:
    listanumeors.append(count)
    count+=1
    if count==101: 
        nuevalista=listanumeors.reverse()
        for lista in listanumeors:
            print(lista)

