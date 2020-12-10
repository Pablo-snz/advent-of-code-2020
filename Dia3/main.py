def dia3A(input):

    with open(input) as f:
        plano = [fila.strip('\n') for fila in f]

    l = len(plano)
    return sum([1 for y, columna in zip(list(range(1,l)), list(range(3,3*l,3)))\
            if plano[y][columna % len(plano[y])] != '.'])   

if __name__ == '__main__':
    print(dia3A('input'))
