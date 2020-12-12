def day5A(raw_data) -> int:
    data = preprocess(raw_data)
    return max([calculateID(positionR(i[:-3]),positionC(i[-3:])) for i in data])


def day5B(raw_data) -> int:
    data = preprocess(raw_data)
    ocupated = [calculateID(positionR(i[:-3]),positionC(i[-3:])) for i in data]
    total = list(range(min(ocupated),max(ocupated)+1))
    return (set(total) - set(ocupated)).pop()


def preprocess(raw_data) -> list:
    with open(raw_data) as f:
        data = [fila.strip('\n') for fila in f]
    return data


def calculateID(r, c) -> int:
    return r*8+c


def positionR(code, trows = 127, tcols = 7) -> tuple:
    row = list(range(trows+1))
    for lettr in code:
        if lettr == 'B':
            row = row[len(row)//2:]
        else:
            row = row[:len(row)//2]
    return row[0]
    

def positionC(code, trows = 127, tcols = 7) -> tuple:
    col = list(range(tcols+1))
    for lettr in code:
        if lettr == 'R':
            col = col[len(col)//2:]
        else:
            col = col[:len(col)//2]

    return col[0]


if __name__ == '__main__':
    print(day5A('input'))
    print(day5B('input'))
