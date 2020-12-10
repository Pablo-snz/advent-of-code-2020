def day2A(input):
    
    with open(input) as f:
        datos = [fila.strip('\n').split(" ") for fila in f]


    minimo = [int(fila[0].split("-")[0]) for fila in  datos]
    maximo = [int(fila[0].split("-")[1]) for fila in datos]
    letra  = [fila[1][0] for fila in datos]
    passwd = [fila[2] for fila in datos]


    return sum([1 for i in range(0, len(passwd))\
            if passwd[i].count(letra[i]) <= maximo[i] and\
            passwd[i].count(letra[i]) >= minimo[i] ])


def day2B(input):
    
    with open(input) as f:
        datos = [fila.strip('\n').split(" ") for fila in f]


    pos1 = [int(fila[0].split("-")[0]) for fila in  datos]
    pos2 = [int(fila[0].split("-")[1]) for fila in datos]
    letra  = [fila[1][0] for fila in datos]
    passwd = [fila[2] for fila in datos]


    return sum([1 for i in range(0, len(passwd))\
            if int(passwd[i][pos1[i]-1] == letra[i]) +\
            int(passwd[i][pos2[i]-1] == letra[i]) == 1])



if __name__ == '__main__':
    print(day2A('input'))
    print(day2B('input'))

