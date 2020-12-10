def dia3A(input):

    with open(input) as f:
        plano = [fila.strip('\n') for fila in f]

    return sum([1 for y in range(1,len(plano))\
            if plano[y][y*3 % len(plano[y])] != '.'])   


def dia3B(input, r,d):
    
    with open(input) as f:
        plano = [fila.strip('\n') for fila in f]
    
    l = len(plano)
    return sum([1 for y, columna in zip(list(range(d,l,d)), list(range(r,r*l,r)))\
            if plano[y][columna % len(plano[y])] == '#'])

if __name__ == '__main__':
    print(dia3A('input'))
    print(dia3B('input',1,1)*dia3B('input',3,1)*dia3B('input',5,1)*dia3B('input',7,1)*dia3B('input',1,2))
