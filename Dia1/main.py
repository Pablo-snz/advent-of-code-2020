

def day1A(input):
    with open(input) as f:
        d = [int(number.strip('\n')) for number in f]

    return [d[i]*d[j] for i in range(0, len(d))\
            for j in range(i+1, len(d)) if d[i]+d[j] == 2020]


def day1B(input):
    with open(input) as f:
        d = [int(number.strip('\n')) for number in f]

    return [d[i]*d[j]*d[w] for i in range(0, len(d))\
            for j in range(i+1, len(d))\
            for w in range(j+1, len(d)) if d[i]+d[j]+d[w] == 2020]


if __name__ == '__main__':
    print(day1A('input'))
    print(day1B('input'))
