


def averages():
    lista = [2.5,7.3,6.5,4.0,5.2 ]
    average = 0
    summa = 0

    for x in range(len(lista)):
        summa = summa + lista[x]


    average = sum(lista) / len(lista)

    print("The average of the elements is", average)

averages()